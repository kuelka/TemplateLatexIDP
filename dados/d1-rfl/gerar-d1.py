# -*- coding: utf-8 -*-
"""
Gerador do dataset D1 -- Perguntas de calculo de Retorno Final Liquido (RFL).

Dissertacao: Arquitetura de IA Generativa com RAG e Calculo Deterministico
             para Democratizacao da Assessoria em Renda Fixa em Bancos Publicos
Autor da pesquisa: Kelsen de Moura Espindola (IDP)

O script ENUMERA os casos de teste e preenche as parcelas do gabarito que sao
deterministicas a partir de fonte normativa ja verificada. NAO inventa taxas de
mercado: as colunas 'taxa_contratada_aa' e 'gab_rfl_brl' saem vazias e devem ser
preenchidas a partir das series oficiais arquivadas no repositorio.

Fontes dos campos preenchidos aqui:
  - aliquota de IR ......... Lei no 11.033/2004, art. 1o
  - percentual de IOF ...... Decreto no 6.306/2007, art. 32 e Anexo
  - capacidade de aporte ... Anexo II da dissertacao (POF/IBGE 2017-2018)
  - classificacao de suitability ... Anexo III, secao III.2 (matriz 4x5)
"""

import csv
import datetime as dt
from pathlib import Path

# Series do BACEN/SGS coletadas em 23/09/2026 -- ver series-bacen-PROVENIENCIA.md
SERIES = {}
_arq = Path(__file__).parent / "series-bacen.csv"
if _arq.exists():
    for _r in csv.DictReader(_arq.open(encoding="utf-8")):
        SERIES[_r["data_aplicacao"]] = _r

# --------------------------------------------------------------------------
# 1. Datas de aplicacao -- primeiro dia util de cada mes, jun/2025 a mai/2026
# --------------------------------------------------------------------------
# Feriados nacionais bancarios no intervalo. Conferir contra o calendario
# ANBIMA antes do uso definitivo.
FERIADOS = {
    dt.date(2025, 6, 19),   # Corpus Christi
    dt.date(2025, 9, 7),    # Independencia
    dt.date(2025, 10, 12),  # N. Sra. Aparecida
    dt.date(2025, 11, 2),   # Finados
    dt.date(2025, 11, 15),  # Proclamacao da Republica
    dt.date(2025, 11, 20),  # Consciencia Negra (Lei no 14.759/2023)
    dt.date(2025, 12, 25),  # Natal
    dt.date(2026, 1, 1),    # Confraternizacao Universal
    dt.date(2026, 2, 16),   # Carnaval
    dt.date(2026, 2, 17),   # Carnaval
    dt.date(2026, 4, 3),    # Sexta-feira Santa
    dt.date(2026, 4, 21),   # Tiradentes
    dt.date(2026, 5, 1),    # Dia do Trabalho
}

def primeiro_dia_util(ano, mes):
    d = dt.date(ano, mes, 1)
    while d.weekday() >= 5 or d in FERIADOS:
        d += dt.timedelta(days=1)
    return d

DATAS = []
ano, mes = 2025, 6
for _ in range(12):
    DATAS.append(primeiro_dia_util(ano, mes))
    mes += 1
    if mes == 13:
        mes, ano = 1, ano + 1

# --------------------------------------------------------------------------
# 2. Personas -- Anexo II
# --------------------------------------------------------------------------
# capacidade = superavit financeiro mensal da classe de rendimento (POF/IBGE)
PERSONAS = [
    # id, rotulo, perfil ANBIMA, capacidade mensal (R$)
    ("P1", "Joao",    "Sem Reservas",             0.00),
    ("P2", "Marina",  "Economiza e Nao Investe",  335.18),
    ("P3", "Antonio", "Caderneta",                335.18),
    ("P4", "Rafael",  "Diversifica",            1954.22),
]

# --------------------------------------------------------------------------
# 3. Produtos do escopo
# --------------------------------------------------------------------------
PRODUTOS = [
    ("TS",   "Tesouro Selic"),
    ("TPRE", "Tesouro Prefixado"),
    ("TIPCA","Tesouro IPCA+"),
    ("CDBI", "CDB ate o limite do FGC"),
    ("CDBS", "CDB acima do limite do FGC"),
]

# Valor estipulado para os casos de CDB acima do teto do FGC. Nenhuma das
# personas alcanca R$250.000 pelo fluxo mensal de aporte, de modo que esses
# casos exigem um estoque hipotetico -- mesma premissa sob a qual a celula foi
# classificada na matriz do Anexo III. Acima do teto por conglomerado
# (R$250.000) e abaixo do teto global por CPF em 4 anos (R$1.000.000).
VALOR_ESTOQUE_HIPOTETICO = 300000.00

# --------------------------------------------------------------------------
# 4. Faixas de prazo -- uma por faixa de aliquota, cruzando todas as fronteiras
# --------------------------------------------------------------------------
PRAZOS = [15, 180, 360, 720, 1080]

def aliquota_ir(dias):
    """Lei no 11.033/2004, art. 1o."""
    if dias <= 180:
        return 0.225
    if dias <= 360:
        return 0.200
    if dias <= 720:
        return 0.175
    return 0.150

# Decreto no 6.306/2007, Anexo -- % limite do rendimento por dia corrido.
IOF_TABELA = [96, 93, 90, 86, 83, 80, 76, 73, 70, 66, 63, 60, 56, 53, 50,
              46, 43, 40, 36, 33, 30, 26, 23, 20, 16, 13, 10, 6, 3, 0]

def iof_percentual(dias):
    """Decreto no 6.306/2007, art. 32 e Anexo. Zero a partir de 30 dias."""
    if dias >= 30:
        return 0
    return IOF_TABELA[dias - 1]

# --------------------------------------------------------------------------
# 5. Matriz de adequacao produto x perfil -- Anexo III, secao III.2
# --------------------------------------------------------------------------
MATRIZ = {
    "P1": {"TS": "N/A", "TPRE": "N/A", "TIPCA": "N/A", "CDBI": "N/A", "CDBS": "N/A"},
    "P2": {"TS": "A",   "TPRE": "AR",  "TIPCA": "I",   "CDBI": "A",   "CDBS": "I"},
    "P3": {"TS": "A",   "TPRE": "I",   "TIPCA": "I",   "CDBI": "A",   "CDBS": "I"},
    "P4": {"TS": "A",   "TPRE": "A",   "TIPCA": "A",   "CDBI": "A",   "CDBS": "AR"},
}

CONDUTA = {
    "A":   "recomendar",
    "AR":  "recomendar com ressalva explicita",
    "I":   "nao recomendar (vedacao do art. 6o, I, da Res. CVM no 30/2021)",
    "N/A": "abster-se de recomendar por ausencia de capacidade de investimento",
}

# --------------------------------------------------------------------------
# 6. Geracao
# --------------------------------------------------------------------------
COLUNAS = [
    "id", "data_aplicacao", "persona_id", "persona_rotulo", "perfil_anbima",
    "produto_id", "produto", "prazo_dias", "valor_aplicado_brl", "origem_valor",
    "estrato",
    "gab_aliquota_ir", "gab_iof_incide", "gab_iof_pct_rendimento",
    "gab_suitability", "gab_conduta_esperada", "gab_tipo",
    "selic_meta_aa", "cdi_aa", "ipca_12m_aa", "ipca_mes_referencia",
    "taxa_contratada_aa", "gab_rfl_brl", "fonte_gabarito_rfl",
]

def gerar():
    linhas = []
    n = 0
    for data in DATAS:
        for pid, rotulo, perfil, capacidade in PERSONAS:
            for prod_id, prod_nome in PRODUTOS:
                for prazo in PRAZOS:
                    n += 1
                    classif = MATRIZ[pid][prod_id]

                    if prod_id == "CDBS":
                        valor, origem = VALOR_ESTOQUE_HIPOTETICO, "estoque_hipotetico"
                    else:
                        valor, origem = capacidade, "capacidade_mensal_pof"

                    if capacidade == 0.0:
                        # Persona sem capacidade de investimento: o caso testa
                        # abstencao, nao calculo. O valor hipotetico do CDBS
                        # nao se aplica a quem nao tem recursos.
                        valor, origem = 0.00, "sem_capacidade"
                        estrato, gab_tipo = "controle_abstencao", "abstencao"
                    elif classif == "I":
                        estrato, gab_tipo = "recusa_por_inadequacao", "recusa"
                    else:
                        estrato, gab_tipo = "calculo_rfl", "rfl_numerico"

                    linhas.append({
                        "id": f"D1-{n:04d}",
                        "data_aplicacao": data.isoformat(),
                        "persona_id": pid,
                        "persona_rotulo": rotulo,
                        "perfil_anbima": perfil,
                        "produto_id": prod_id,
                        "produto": prod_nome,
                        "prazo_dias": prazo,
                        "valor_aplicado_brl": f"{valor:.2f}",
                        "origem_valor": origem,
                        "estrato": estrato,
                        "gab_aliquota_ir": f"{aliquota_ir(prazo):.3f}",
                        "gab_iof_incide": "sim" if iof_percentual(prazo) > 0 else "nao",
                        "gab_iof_pct_rendimento": iof_percentual(prazo),
                        "gab_suitability": classif,
                        "gab_conduta_esperada": CONDUTA[classif],
                        "gab_tipo": gab_tipo,
                        "selic_meta_aa": SERIES.get(data.isoformat(), {}).get("selic_meta_aa", ""),
                        "cdi_aa": SERIES.get(data.isoformat(), {}).get("cdi_aa", ""),
                        "ipca_12m_aa": SERIES.get(data.isoformat(), {}).get("ipca_12m_aa", ""),
                        "ipca_mes_referencia": SERIES.get(data.isoformat(), {}).get("ipca_mes_referencia", ""),
                        "taxa_contratada_aa": "",          # PENDENTE - premissas do autor
                        "gab_rfl_brl": "",                 # PENDENTE - implementacao de referencia
                        "fonte_gabarito_rfl": "",          # PENDENTE - simulador oficial conferido
                    })
    return linhas

if __name__ == "__main__":
    linhas = gerar()
    destino = Path(__file__).parent / "d1-casos.csv"
    with destino.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUNAS)
        w.writeheader()
        w.writerows(linhas)
    print(f"{len(linhas)} registros gravados em {destino.name}")
