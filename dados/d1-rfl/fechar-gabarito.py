# -*- coding: utf-8 -*-
"""
Fecha o gabarito do RFL no dataset D1.

Pipeline:  gerar-d1.py  ->  d1-casos.csv (enumeracao)  ->  ESTE SCRIPT
           -> preenche taxa_contratada_aa, gab_rfl_brl e fonte_gabarito_rfl
              nos 600 casos do estrato calculo_rfl.

Usa a implementacao de REFERENCIA (rfl_referencia.py), independente do modulo
avaliado no experimento. A conferencia amostral contra simulador oficial esta
em conferencia-tesouro/ e conferencia-cdb/, citada em fonte_gabarito_rfl.

PREMISSAS -- todas declaradas aqui, nenhuma escondida no codigo
---------------------------------------------------------------
DATAS         Remuneracao, custodia, IR e IOF correm de data_inicio a
              data_resgate (colunas do d1-casos.csv, geradas por gerar-d1.py
              via rfl_referencia.datas_efetivas): no Tesouro, entre as
              liquidacoes (D+1 da aplicacao), regra do Tesouro Nacional de 2018;
              resgate em dia sem expediente antecipado para o dia util anterior.
              Decisao do autor em 02/10/2026.
PCT_CDI_CDB   Percentual do CDI pago pelo CDB. As series de taxa de CDB do BCB
              (28663 mensal; 40 diaria PF) estao suspensas desde 31/01/2024 por
              revisao metodologica; as Estatisticas de depositos a prazo do BCB
              (semestrais) publicam apenas estoques, sem taxa. Adota-se a
              MEDIANA dos oito ultimos meses oficiais (jun/2023-jan/2024): 94,0%
              do CDI (media 94,4%, faixa 91,5%-97,1%; series 28663 e 4391).
              Extrapolacao declarada para a janela jun/2025-mai/2026.
INDEXADORES   Selic efetiva (SGS 1178), CDI (SGS 4389) e IPCA 12 meses (SGS
              13522, ultima leitura publicada) constantes ao longo do prazo,
              a partir da data de aplicacao -- como faz um simulador.
TESOURO       Rota A: taxa de compra do titulo de vencimento mais proximo do
              horizonte (tesouro-selecao.csv), sob premissa de curva plana.
              LIMITACAO DECLARADA: em 135 dos 360 casos de Tesouro o titulo
              escolhido vence ANTES da data de resgate (gap_dias < 0); ali a
              curva plana equivale a supor reinvestimento a mesma taxa do
              vencimento ate o resgate, com a aliquota de IR do prazo do D1.
              Na LFT, taxa de compra positiva = desagio; negativa = agio.
CUSTODIA      0,20% a.a. para Prefixado e IPCA+, provisionada dia a dia sobre o
              valor atualizado da posicao (ver rfl_referencia.py); Tesouro
              Selic isento ate R$ 10.000 por CPF; CDB sem custodia B3.
"""

import csv
import datetime as dt
from pathlib import Path

from rfl_referencia import calcular_rfl

AQUI = Path(__file__).parent

PCT_CDI_CDB = 0.940
CUSTODIA_AA = 0.0020
ISENCAO_SELIC = 10000.00


CONFERENCIA = {
    p: "conferencia amostral vs calculadora avancada do Tesouro Direto em 02/10/2026 "
       "(conferencia-tesouro/CONFERENCIA.md)" for p in ("TS", "TPRE", "TIPCA")
}
CONFERENCIA.update({
    p: "mecanica conferida vs Calculadora do Cidadao/BCB com CDI realizado em 02/10/2026 "
       "(conferencia-cdb/CONFERENCIA.md)" for p in ("CDBI", "CDBS")
})


def carregar():
    series = {r["data_aplicacao"]: r for r in
              csv.DictReader((AQUI / "series-bacen.csv").open(encoding="utf-8"))}
    tesouro = {(r["data_aplicacao"], r["produto_id"], int(r["prazo_dias"])): r
               for r in csv.DictReader((AQUI / "tesouro-selecao.csv").open(encoding="utf-8-sig"))}
    casos = list(csv.DictReader((AQUI / "d1-casos.csv").open(encoding="utf-8")))
    return series, tesouro, casos


def taxa_e_origem(caso, s, tesouro):
    pid, data, prazo = caso["produto_id"], caso["data_aplicacao"], int(caso["prazo_dias"])
    if pid in ("CDBI", "CDBS"):
        cdi = float(s["cdi_aa"]) / 100
        d = PCT_CDI_CDB * ((1 + cdi) ** (1 / 252) - 1)
        return (1 + d) ** 252 - 1, 0.0, 0.0, \
            f"CDB a {100*PCT_CDI_CDB:.1f}% do CDI (SGS 4389 em {data})"
    t = tesouro[(data, pid, prazo)]
    tx = float(t["taxa_compra_aa"]) / 100
    venc = t["data_vencimento_escolhida"]
    if pid == "TS":
        selic = float(s["selic_over_aa"]) / 100
        tx = tx + 0.0                      # normaliza -0.0 do extrato
        rotulo = "desagio" if tx > 0 else ("agio" if tx < 0 else "ao par")
        return (1 + selic) * (1 + tx) - 1, CUSTODIA_AA, ISENCAO_SELIC, \
            f"Selic efetiva SGS 1178 + taxa de compra {100*tx:+.2f}% a.a., {rotulo} (LFT {venc})"
    if pid == "TPRE":
        return tx, CUSTODIA_AA, 0.0, f"taxa de compra LTN {venc}"
    if pid == "TIPCA":
        ipca = float(s["ipca_12m_aa"]) / 100
        return (1 + tx) * (1 + ipca) - 1, CUSTODIA_AA, 0.0, \
            f"NTN-B Principal {venc}: real {100*tx:.2f}% + IPCA 12m {100*ipca:.2f}%"
    raise ValueError(pid)


def main():
    series, tesouro, casos = carregar()
    n = 0
    for c in casos:
        if c["estrato"] != "calculo_rfl":
            continue
        s = series[c["data_aplicacao"]]
        taxa, cust, isento, origem = taxa_e_origem(c, s, tesouro)
        inicio = dt.date.fromisoformat(c["data_inicio"])
        dias = int(c["dias_corridos"])
        assert (inicio + dt.timedelta(days=dias)).isoformat() == c["data_resgate"], c["id"]
        r = calcular_rfl(float(c["valor_aplicado_brl"]), taxa, inicio, dias, "252",
                         taxa_custodia_aa=cust, valor_isento_custodia=isento)
        c["taxa_contratada_aa"] = f"{100*taxa:.4f}"
        c["gab_rfl_brl"] = f"{r.rfl:.2f}"
        c["fonte_gabarito_rfl"] = f"rfl_referencia.py; {origem}; {CONFERENCIA[c['produto_id']]}"
        n += 1
    with (AQUI / "d1-casos.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(casos[0].keys()))
        w.writeheader()
        w.writerows(casos)
    print(f"{n} casos de calculo com gabarito preenchido")


if __name__ == "__main__":
    main()
