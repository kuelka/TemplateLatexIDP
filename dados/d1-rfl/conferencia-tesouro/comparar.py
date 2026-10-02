# -*- coding: utf-8 -*-
"""
Conferencia amostral do gabarito do D1 contra a calculadora avancada do
Tesouro Direto (https://www.tesourodireto.com.br/simuladores/calculadora-avancada).

Entradas (nesta pasta):
  api-requisicoes.json  corpo enviado a POST /o/calculadora-avancada, por caso
                        (purchsDt = data_aplicacao; redDt = data_resgate do D1)
  api-resultados.json   resposta da calculadora, por caso (ver CONFERENCIA.md)

Saida:
  comparacao.csv        componentes do RFL lado a lado, por caso
  resumo impresso na tela

Uso:  cd dados/d1-rfl/conferencia-tesouro && python3 comparar.py
Nao altera o d1-casos.csv.
"""

import csv
import datetime as dt
import importlib.util
import json
import statistics as st
import sys
from pathlib import Path

AQUI = Path(__file__).parent
D1 = AQUI.parent
sys.path.insert(0, str(D1))
from rfl_referencia import calcular_rfl, eh_dia_util, proximo_dia_util  # noqa: E402

_spec = importlib.util.spec_from_file_location("fg", D1 / "fechar-gabarito.py")
fg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fg)
series, tesouro, casos = fg.carregar()
casos = {c["id"]: c for c in casos}

# id, dias corridos, dias uteis, bruto, custodia, aliquota IR (%), IR, liquido, status, data/hora
api = json.load((AQUI / "api-resultados.json").open(encoding="utf-8"))


def resumo(nome, xs):
    xs = list(xs)
    return (
        f"{nome}: n={len(xs)} min={min(xs):+.2f} "
        f"mediana={st.median(xs):+.2f} max={max(xs):+.2f}"
    )


def du_calculadora(inicio, resgate):
    """Dias uteis no intervalo [inicio, D+1 util do resgate), com 20/11 tratado
    como dia util: a convencao que reproduz a calculadora (ver CONFERENCIA.md).
    A referencia conta [inicio, resgate), com o resgate liquidando no proprio dia."""

    def util(d):
        if d.month == 11 and d.day == 20 and d.weekday() < 5:
            return True
        return eh_dia_util(d)

    fim = proximo_dia_util(resgate)
    return sum(
        1 for k in range((fim - inicio).days) if util(inicio + dt.timedelta(days=k))
    )


linhas = []
for id_, dc, du, bruto, cust, aliq, ir, liq, status, _ in api:
    assert status == "0", id_
    c = casos[id_]
    v = float(c["valor_aplicado_brl"])
    inicio = dt.date.fromisoformat(c["data_inicio"])
    resgate = dt.date.fromisoformat(c["data_resgate"])
    dias = int(c["dias_corridos"])
    taxa, cust_aa, isento, _o = fg.taxa_e_origem(
        c, series[c["data_aplicacao"]], tesouro
    )
    r = calcular_rfl(
        v,
        taxa,
        inicio,
        dias,
        "252",
        taxa_custodia_aa=cust_aa,
        valor_isento_custodia=isento,
    )
    assert f"{r.rfl:.2f}" == c["gab_rfl_brl"], id_
    linhas.append(
        dict(
            id=id_,
            produto=c["produto_id"],
            prazo=int(c["prazo_dias"]),
            valor=v,
            dias_corridos_ref=dias,
            dias_corridos_api=dc,
            du_ref=r.dias_uteis,
            du_api=du,
            du_convencao_api=du_calculadora(inicio, resgate),
            bruto_ref=r.montante_bruto,
            bruto_api=bruto,
            bruto_ref_com_du_api=v * (1 + taxa) ** (du / 252),
            custodia_ref=r.custodia,
            custodia_api=cust,
            iof_ref=r.iof,
            aliquota_ref=100 * r.aliquota_ir,
            aliquota_api=aliq,
            ir_ref=r.ir,
            ir_api=ir,
            ir_api_recalculado=round(aliq / 100 * (bruto - v), 2),
            rfl_ref=r.rfl,
            rfl_api=liq - v,
        )
    )

print(f"casos comparados: {len(linhas)}")
print(
    "dias corridos (prazo do IR) iguais:",
    sum(l["dias_corridos_ref"] == l["dias_corridos_api"] for l in linhas),
    "de",
    len(linhas),
)
print(
    "aliquota de IR igual em todos:",
    all(abs(l["aliquota_ref"] - l["aliquota_api"]) < 1e-9 for l in linhas),
)
print(
    "IR da calculadora = aliquota x (bruto - aplicado), custodia fora da base:",
    all(abs(l["ir_api"] - l["ir_api_recalculado"]) < 0.015 for l in linhas),
)
ddu = [l["du_api"] - l["du_ref"] for l in linhas]
print(
    "dias uteis (calculadora - referencia):",
    {k: ddu.count(k) for k in sorted(set(ddu))},
)
print(
    "dias uteis explicados por [inicio, D+1 do resgate) com 20/11 util:",
    sum(l["du_convencao_api"] == l["du_api"] for l in linhas),
    "de",
    len(linhas),
)
print(
    resumo(
        "bruto (calculadora - referencia)",
        (l["bruto_api"] - l["bruto_ref"] for l in linhas),
    )
)
print(
    resumo(
        "bruto (calculadora - referencia com os dias uteis da calculadora)",
        (l["bruto_api"] - l["bruto_ref_com_du_api"] for l in linhas),
    )
)
for p in ("TPRE", "TIPCA", "TS"):
    sub = [l for l in linhas if l["produto"] == p]
    print(f"[{p}] n={len(sub)}")
    print(
        "  "
        + resumo(
            "custodia (calculadora - referencia)",
            (l["custodia_api"] - l["custodia_ref"] for l in sub),
        )
    )
    print(
        "  "
        + resumo(
            "RFL (calculadora - referencia)", (l["rfl_api"] - l["rfl_ref"] for l in sub)
        )
    )
print(
    resumo(
        "IOF da referencia nos casos de 15 dias (a calculadora nao aplica IOF)",
        (l["iof_ref"] for l in linhas if l["prazo"] == 15),
    )
)

with (AQUI / "comparacao.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(linhas[0].keys()))
    w.writeheader()
    for l in linhas:
        w.writerow(
            {k: (f"{x:.4f}" if isinstance(x, float) else x) for k, x in l.items()}
        )
