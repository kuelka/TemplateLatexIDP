# -*- coding: utf-8 -*-
"""
Implementacao de REFERENCIA do Retorno Final Liquido (RFL).

PAPEL NO EXPERIMENTO
--------------------
Este modulo produz o GABARITO do dataset D1. Ele e, e deve permanecer,
INDEPENDENTE do modulo Python do objetivo especifico (c) -- aquele que o agente
chama por function calling e que o experimento avalia. Se o gabarito saisse do
proprio modulo sob teste, a taxa de erro medida seria trivialmente zero e o
experimento nao testaria nada.

Regra pratica: nenhuma linha deste arquivo deve ser importada pelo modulo do
objetivo (c), nem o contrario. Sao duas implementacoes que se conferem
mutuamente, e ambas devem ser conferidas por amostragem contra simuladores
oficiais (Tesouro Direto, calculadoras ANBIMA).

BASE NORMATIVA (conferida em texto oficial -- ver bibliografia/base-legal-rfl.md)
---------------------------------------------------------------------------
IR  : Lei no 11.033/2004, art. 1o -- 22,5% / 20% / 17,5% / 15%
IOF : Decreto no 6.306/2007, art. 32 e Anexo -- sobre o RENDIMENTO, nunca sobre
      o principal, zerando a partir do 30o dia corrido

PREMISSAS AINDA NAO DECLARADAS PELO AUTOR
-----------------------------------------
Estao expostas como PARAMETROS, sem valor default silencioso, justamente para
nao serem decididas por omissao:
  - convencao de capitalizacao ("252" ou "365")
  - percentual do CDI adotado para o CDB
  - taxa de custodia da B3
A ordem de incidencia entre custodia e IR tambem e premissa: aqui a custodia e
deduzida do montante bruto ANTES da apuracao da base tributavel.
"""

import datetime as dt
from dataclasses import dataclass

# ---------------------------------------------------------------------------
# Feriados
# ---------------------------------------------------------------------------
# Calculados, nao digitados: as datas moveis derivam da Pascoa (algoritmo de
# Meeus/Jones/Butcher). CONFERIR contra o calendario oficial da ANBIMA antes do
# uso definitivo -- Carnaval e Corpus Christi nao sao feriados nacionais por lei
# federal, mas sao dias sem expediente bancario e entram no calendario ANBIMA.

def pascoa(ano):
    a = ano % 19
    b, c = divmod(ano, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mes, dia = divmod(h + l - 7 * m + 114, 31)
    return dt.date(ano, mes, dia + 1)


def feriados_nacionais(ano):
    p = pascoa(ano)
    return {
        dt.date(ano, 1, 1):    "Confraternizacao Universal",
        p - dt.timedelta(48):  "Carnaval (segunda)",
        p - dt.timedelta(47):  "Carnaval (terca)",
        p - dt.timedelta(2):   "Sexta-feira Santa",
        dt.date(ano, 4, 21):   "Tiradentes",
        dt.date(ano, 5, 1):    "Dia do Trabalho",
        p + dt.timedelta(60):  "Corpus Christi",
        dt.date(ano, 9, 7):    "Independencia",
        dt.date(ano, 10, 12):  "N. Sra. Aparecida",
        dt.date(ano, 11, 2):   "Finados",
        dt.date(ano, 11, 15):  "Proclamacao da Republica",
        dt.date(ano, 11, 20):  "Consciencia Negra (Lei no 14.759/2023)",
        dt.date(ano, 12, 25):  "Natal",
    }


_CACHE = {}

def eh_dia_util(d):
    if d.weekday() >= 5:
        return False
    if d.year not in _CACHE:
        _CACHE[d.year] = feriados_nacionais(d.year)
    return d not in _CACHE[d.year]


def dias_uteis(inicio, fim):
    """Dias uteis no intervalo [inicio, fim) -- convencao de contagem de
    remuneracao: conta-se o dia da aplicacao, nao o do resgate."""
    if fim <= inicio:
        return 0
    n, d = 0, inicio
    while d < fim:
        if eh_dia_util(d):
            n += 1
        d += dt.timedelta(days=1)
    return n


# ---------------------------------------------------------------------------
# Tabelas tributarias
# ---------------------------------------------------------------------------
def aliquota_ir(dias_corridos):
    """Lei no 11.033/2004, art. 1o."""
    if dias_corridos <= 180:
        return 0.225
    if dias_corridos <= 360:
        return 0.200
    if dias_corridos <= 720:
        return 0.175
    return 0.150


_IOF = [96, 93, 90, 86, 83, 80, 76, 73, 70, 66, 63, 60, 56, 53, 50,
        46, 43, 40, 36, 33, 30, 26, 23, 20, 16, 13, 10, 6, 3, 0]

def iof_percentual(dias_corridos):
    """Decreto no 6.306/2007, art. 32 e Anexo. Percentual LIMITE do rendimento."""
    if dias_corridos >= 30:
        return 0.0
    if dias_corridos < 1:
        raise ValueError("prazo minimo de 1 dia")
    return _IOF[dias_corridos - 1] / 100.0


# ---------------------------------------------------------------------------
# Calculo
# ---------------------------------------------------------------------------
@dataclass
class ResultadoRFL:
    valor_aplicado: float
    dias_corridos: int
    dias_uteis: int
    montante_bruto: float
    custodia: float
    rendimento_tributavel: float
    iof_pct: float
    iof: float
    aliquota_ir: float
    ir: float
    valor_liquido: float
    rfl: float                # valor_liquido - valor_aplicado

    def como_dict(self):
        return {k: (round(v, 8) if isinstance(v, float) else v)
                for k, v in self.__dict__.items()}


def calcular_rfl(valor_aplicado, taxa_aa, data_aplicacao, dias_corridos,
                 convencao, taxa_custodia_aa=0.0):
    """
    valor_aplicado : R$ aplicados
    taxa_aa        : taxa contratada em % a.a. na forma decimal (0.1475 = 14,75%)
    data_aplicacao : datetime.date
    dias_corridos  : prazo do caso do D1 (define IR e IOF)
    convencao      : "252" (dias uteis, padrao do mercado brasileiro) ou
                     "365" (dias corridos). PREMISSA DO AUTOR -- sem default.
    taxa_custodia_aa : taxa de custodia da B3 em decimal. PREMISSA DO AUTOR.

    Ordem de incidencia adotada: capitalizacao -> custodia -> IOF -> IR.
    """
    if convencao not in ("252", "365"):
        raise ValueError('convencao deve ser "252" ou "365" -- premissa do autor')

    data_resgate = data_aplicacao + dt.timedelta(days=dias_corridos)
    du = dias_uteis(data_aplicacao, data_resgate)

    if convencao == "252":
        expoente = du / 252.0
    else:
        expoente = dias_corridos / 365.0

    montante = valor_aplicado * (1.0 + taxa_aa) ** expoente
    custodia = valor_aplicado * ((1.0 + taxa_custodia_aa) ** expoente - 1.0) \
        if taxa_custodia_aa else 0.0

    rendimento = montante - custodia - valor_aplicado
    if rendimento < 0:
        rendimento = 0.0

    pct_iof = iof_percentual(dias_corridos)
    iof = rendimento * pct_iof
    aliq = aliquota_ir(dias_corridos)
    ir = (rendimento - iof) * aliq

    liquido = valor_aplicado + rendimento - iof - ir

    return ResultadoRFL(
        valor_aplicado=valor_aplicado, dias_corridos=dias_corridos, dias_uteis=du,
        montante_bruto=montante, custodia=custodia,
        rendimento_tributavel=rendimento, iof_pct=pct_iof, iof=iof,
        aliquota_ir=aliq, ir=ir, valor_liquido=liquido,
        rfl=liquido - valor_aplicado)


# ---------------------------------------------------------------------------
# Autoteste
# ---------------------------------------------------------------------------
def _autoteste():
    ok = 0
    falhas = []

    def checa(nome, obtido, esperado, tol=1e-9):
        nonlocal ok
        if abs(obtido - esperado) <= tol:
            ok += 1
        else:
            falhas.append(f"{nome}: obtido {obtido!r}, esperado {esperado!r}")

    # --- Pascoa e feriados moveis, conferiveis em calendario ---------------
    checa("pascoa 2025", pascoa(2025).toordinal(), dt.date(2025, 4, 20).toordinal())
    checa("pascoa 2026", pascoa(2026).toordinal(), dt.date(2026, 4, 5).toordinal())
    checa("sexta santa 2026", (pascoa(2026) - dt.timedelta(2)).toordinal(),
          dt.date(2026, 4, 3).toordinal())
    checa("carnaval 2026 seg", (pascoa(2026) - dt.timedelta(48)).toordinal(),
          dt.date(2026, 2, 16).toordinal())
    checa("corpus christi 2025", (pascoa(2025) + dt.timedelta(60)).toordinal(),
          dt.date(2025, 6, 19).toordinal())

    # --- dias uteis: feriado e fim de semana nao contam --------------------
    checa("du 01-08/01/2026", dias_uteis(dt.date(2026, 1, 1), dt.date(2026, 1, 8)), 4)
    checa("du intervalo vazio", dias_uteis(dt.date(2026, 1, 5), dt.date(2026, 1, 5)), 0)

    # --- fronteiras de IR --------------------------------------------------
    for d, esp in ((180, 0.225), (181, 0.200), (360, 0.200),
                   (361, 0.175), (720, 0.175), (721, 0.150)):
        checa(f"IR {d}d", aliquota_ir(d), esp)

    # --- fronteiras de IOF -------------------------------------------------
    checa("IOF 1d", iof_percentual(1), 0.96)
    checa("IOF 15d", iof_percentual(15), 0.50)
    checa("IOF 29d", iof_percentual(29), 0.03)
    checa("IOF 30d", iof_percentual(30), 0.0)

    # --- caso fechado a mao: 365 corridos, conv. 365, sem custodia ---------
    # 1000 * 1.10^(365/365) = 1100 ; rendimento 100 ; IOF 0.
    # ATENCAO: 365 dias cai na faixa "361 a 720" -> 17,5%, NAO 20%. A faixa de
    # 20% termina no 360o dia. IR = 17,50 ; liquido = 1082,50.
    r = calcular_rfl(1000.0, 0.10, dt.date(2025, 6, 2), 365, "365")
    checa("montante", r.montante_bruto, 1100.0, 1e-9)
    checa("rendimento", r.rendimento_tributavel, 100.0, 1e-9)
    checa("iof", r.iof, 0.0)
    checa("aliquota", r.aliquota_ir, 0.175)
    checa("ir", r.ir, 17.5, 1e-9)
    checa("liquido", r.valor_liquido, 1082.5, 1e-9)
    checa("rfl", r.rfl, 82.5, 1e-9)

    # --- o mesmo caso exatamente no 360o dia, onde a aliquota ainda e 20% ---
    r3 = calcular_rfl(1000.0, 0.10, dt.date(2025, 6, 2), 360, "365")
    checa("aliquota 360d", r3.aliquota_ir, 0.20)

    # --- IOF corta a base do IR (15 dias) ---------------------------------
    r2 = calcular_rfl(1000.0, 0.10, dt.date(2025, 6, 2), 15, "365")
    rend = 1000.0 * (1.10 ** (15 / 365.0)) - 1000.0
    checa("iof 15d valor", r2.iof, rend * 0.50, 1e-9)
    checa("ir apos iof", r2.ir, (rend - rend * 0.50) * 0.225, 1e-9)

    # --- convencao invalida deve falhar -----------------------------------
    try:
        calcular_rfl(1000.0, 0.10, dt.date(2025, 6, 2), 180, "360")
        falhas.append("convencao invalida nao levantou erro")
    except ValueError:
        ok += 1

    print(f"autoteste: {ok} verificacoes OK, {len(falhas)} falhas")
    for f in falhas:
        print("  FALHA:", f)
    return not falhas


if __name__ == "__main__":
    import sys
    sys.exit(0 if _autoteste() else 1)
