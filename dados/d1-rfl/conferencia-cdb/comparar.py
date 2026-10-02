# -*- coding: utf-8 -*-
"""
Conferencia da mecanica do CDB do D1 contra a Calculadora do Cidadao do BCB
(Correcao de valores > CDI, https://www3.bcb.gov.br/CALCIDADAO/).

A calculadora usa o CDI REALIZADO; o gabarito do D1 projeta o CDI constante a
partir da aplicacao. Por isso o que se confere aqui e a mecanica -- % do CDI
sobre a taxa diaria, calendario de dias uteis e convencao [inicio, fim) --,
aplicando a regra de capitalizacao do gabarito ao CDI realizado (SGS 12).

Uso:  cd dados/d1-rfl/conferencia-cdb && python3 comparar.py
"""

import datetime as dt
import json
import sys
from pathlib import Path

AQUI = Path(__file__).parent
sys.path.insert(0, str(AQUI.parent))
from rfl_referencia import dias_uteis, eh_dia_util  # noqa: E402

PCT_CDI = 0.94  # mesma premissa do fechar-gabarito.py

serie = json.load((AQUI / "cdi-sgs12.json").open(encoding="utf-8"))
trechos = [(dt.date.fromisoformat(d), v / 100) for d, v in serie["trechos"]]
ini_serie = dt.date.fromisoformat(serie["primeira_data"])
fim_serie = dt.date.fromisoformat(serie["ultima_data"])
assert dias_uteis(ini_serie, fim_serie + dt.timedelta(days=1)) == serie["observacoes"]


def cdi_dia(d):
    return [v for inicio, v in trechos if d >= inicio][-1]


def br(s):
    return dt.date(int(s[6:]), int(s[3:5]), int(s[:2]))


casos = json.load((AQUI / "calculadora-cidadao.json").open(encoding="utf-8"))
maior = 0.0
print("aplicacao   resgate D1  inicio usado  fim usado    du   referencia   calculadora")
for aplic, resg, ini, fim, indice in casos:
    i, f = br(ini), br(fim)
    fator, n, d = 1.0, 0, i
    while d < f:
        if eh_dia_util(d):
            fator *= 1 + PCT_CDI * cdi_dia(d)
            n += 1
        d += dt.timedelta(days=1)
    oficial = float(indice.replace(",", "."))
    maior = max(maior, abs(fator - oficial))
    print(f"{aplic}  {resg}  {ini}    {fim}  {n:4d}   {fator:.8f}   {oficial:.8f}")
print(f"\n{len(casos)} periodos; maior diferenca absoluta no indice: {maior:.1e}")
