# -*- coding: utf-8 -*-
"""
Extrai do arquivo historico do Tesouro Transparente apenas o recorte necessario
ao dataset D1, evitando versionar dezenas de megabytes no repositorio.

Uso:
    python3 extrair-tesouro.py /caminho/para/precotaxatesourodireto.csv

Saidas, gravadas ao lado deste script:
    tesouro-12datas.csv    -- todas as linhas dos titulos do escopo nas 12 datas
                              de aplicacao (extrato auditavel, poucas centenas de linhas)
    tesouro-selecao.csv    -- um titulo escolhido por (data, tipo, prazo alvo):
                              o de vencimento mais proximo do horizonte
    tesouro-PROVENIENCIA.txt -- checksum do arquivo original, data e diagnostico

ATENCAO: este script NAO foi executado contra o arquivo real -- ele nao esta
acessivel do ambiente onde foi escrito. Ele detecta e IMPRIME o cabecalho que
encontrar e aborta com mensagem clara se alguma coluna esperada faltar. Se o
layout divergir, ajuste o dicionario COLUNAS abaixo; nada mais precisa mudar.
"""

import csv
import datetime as dt
import hashlib
import sys
import unicodedata
from pathlib import Path

AQUI = Path(__file__).parent

# ---------------------------------------------------------------------------
# Titulos do escopo. As variantes "com Juros Semestrais" (NTN-F e NTN-B com
# cupom) ficam DE FORA de proposito: o escopo da dissertacao sao os titulos de
# fluxo unico, e incluir os de cupom quebraria a correspondencia com a matriz
# de adequacao do Anexo III.
TIPOS_ESCOPO = {
    "tesouro selic": "TS",
    "tesouro prefixado": "TPRE",
    "tesouro ipca+": "TIPCA",
}

PRAZOS = [15, 180, 360, 720, 1080]

# Nomes de coluna esperados, ja normalizados (sem acento, minusculos, sem
# espacos duplicados). Ajuste aqui se o cabecalho real divergir.
COLUNAS = {
    "tipo":       "tipo titulo",
    "vencimento": "data vencimento",
    "base":       "data base",
    "taxa_compra": "taxa compra manha",
    "pu_compra":   "pu compra manha",
}


def normalizar(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return " ".join(s.lower().replace('"', "").split())


def ler_datas_do_d1():
    """As 12 datas vem do proprio d1-casos.csv, para nao haver divergencia."""
    p = AQUI / "d1-casos.csv"
    if not p.exists():
        sys.exit(f"ERRO: {p.name} nao encontrado ao lado deste script.")
    with p.open(encoding="utf-8") as f:
        datas = sorted({r["data_aplicacao"] for r in csv.DictReader(f)})
    if len(datas) != 12:
        sys.exit(f"ERRO: esperadas 12 datas em d1-casos.csv, encontradas {len(datas)}.")
    return [dt.date.fromisoformat(d) for d in datas]


def abrir(caminho):
    """Tenta utf-8-sig e cai para latin-1, que e o encoding usual do arquivo."""
    for enc in ("utf-8-sig", "latin-1"):
        try:
            f = open(caminho, encoding=enc, newline="")
            f.readline()
            f.seek(0)
            return f, enc
        except UnicodeDecodeError:
            continue
    sys.exit("ERRO: nao foi possivel decodificar o arquivo em utf-8 nem latin-1.")


def detectar_separador(linha):
    return ";" if linha.count(";") > linha.count(",") else ","


def num(s):
    """Converte '14,65' ou '14.65' em float. Devolve None se vazio."""
    s = (s or "").strip().replace('"', "")
    if not s:
        return None
    if "," in s and "." in s:
        s = s.replace(".", "")          # separador de milhar
    return float(s.replace(",", "."))


def data_br(s):
    s = (s or "").strip().replace('"', "")
    for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d/%m/%y"):
        try:
            return dt.datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    origem = Path(sys.argv[1]).expanduser()
    if not origem.exists():
        sys.exit(f"ERRO: arquivo nao encontrado: {origem}")

    datas = ler_datas_do_d1()
    datas_set = set(datas)

    # checksum do arquivo original, em blocos (o arquivo e grande)
    h = hashlib.sha256()
    with origem.open("rb") as fb:
        for bloco in iter(lambda: fb.read(1 << 20), b""):
            h.update(bloco)
    sha = h.hexdigest()

    f, enc = abrir(origem)
    sep = detectar_separador(f.readline())
    f.seek(0)
    leitor = csv.reader(f, delimiter=sep)
    cabecalho = next(leitor)
    norm = [normalizar(c) for c in cabecalho]

    print(f"encoding detectado : {enc}")
    print(f"separador detectado: {sep!r}")
    print(f"cabecalho encontrado ({len(cabecalho)} colunas):")
    for c in cabecalho:
        print(f"   - {c}")

    idx = {}
    faltando = []
    for chave, esperado in COLUNAS.items():
        if esperado in norm:
            idx[chave] = norm.index(esperado)
        else:
            faltando.append(esperado)
    if faltando:
        sys.exit("\nERRO: colunas esperadas ausentes: " + ", ".join(faltando) +
                 "\nAjuste o dicionario COLUNAS no topo do script com os nomes reais acima.")

    selecionadas = []
    lidas = 0
    for linha in leitor:
        lidas += 1
        if len(linha) <= max(idx.values()):
            continue
        tipo_norm = normalizar(linha[idx["tipo"]])
        if tipo_norm not in TIPOS_ESCOPO:
            continue
        base = data_br(linha[idx["base"]])
        if base not in datas_set:
            continue
        venc = data_br(linha[idx["vencimento"]])
        selecionadas.append({
            "data_base": base.isoformat(),
            "produto_id": TIPOS_ESCOPO[tipo_norm],
            "tipo_titulo": linha[idx["tipo"]].strip(),
            "data_vencimento": venc.isoformat() if venc else "",
            "taxa_compra_aa": num(linha[idx["taxa_compra"]]),
            "pu_compra": num(linha[idx["pu_compra"]]),
        })

    print(f"\nlinhas lidas      : {lidas}")
    print(f"linhas no recorte : {len(selecionadas)}")
    if not selecionadas:
        sys.exit("ERRO: nenhuma linha casou. Confira TIPOS_ESCOPO e o formato das datas.")

    saida1 = AQUI / "tesouro-12datas.csv"
    with saida1.open("w", newline="", encoding="utf-8") as g:
        w = csv.DictWriter(g, fieldnames=list(selecionadas[0].keys()))
        w.writeheader()
        w.writerows(selecionadas)

    # --- selecao por prazo: vencimento mais proximo do horizonte alvo --------
    escolhas = []
    for data in datas:
        for tipo_norm, pid in TIPOS_ESCOPO.items():
            cands = [s for s in selecionadas
                     if s["data_base"] == data.isoformat()
                     and s["produto_id"] == pid and s["data_vencimento"]]
            if not cands:
                continue
            for prazo in PRAZOS:
                alvo = data + dt.timedelta(days=prazo)
                melhor = min(cands, key=lambda s: abs(
                    (dt.date.fromisoformat(s["data_vencimento"]) - alvo).days))
                gap = (dt.date.fromisoformat(melhor["data_vencimento"]) - alvo).days
                escolhas.append({
                    "data_aplicacao": data.isoformat(),
                    "produto_id": pid,
                    "prazo_dias": prazo,
                    "data_vencimento_escolhida": melhor["data_vencimento"],
                    "gap_dias": gap,
                    "taxa_compra_aa": melhor["taxa_compra_aa"],
                    "pu_compra": melhor["pu_compra"],
                })

    saida2 = AQUI / "tesouro-selecao.csv"
    with saida2.open("w", newline="", encoding="utf-8") as g:
        w = csv.DictWriter(g, fieldnames=list(escolhas[0].keys()))
        w.writeheader()
        w.writerows(escolhas)

    gaps = [abs(e["gap_dias"]) for e in escolhas]
    gaps.sort()
    print(f"\nselecoes geradas  : {len(escolhas)}")
    print(f"descasamento entre vencimento e horizonte alvo, em dias:")
    print(f"   minimo {gaps[0]} | mediana {gaps[len(gaps)//2]} | maximo {gaps[-1]}")
    print("   -> leia a secao 'O problema do vencimento' no COMO-EXTRAIR-TESOURO.md")

    prov = AQUI / "tesouro-PROVENIENCIA.txt"
    prov.write_text(
        "Extrato do Tesouro Transparente para o dataset D1\n"
        f"Data da extracao ... {dt.date.today().isoformat()}\n"
        f"Arquivo de origem .. {origem.name}\n"
        f"Tamanho ............ {origem.stat().st_size} bytes\n"
        f"SHA-256 ............ {sha}\n"
        "Fonte .............. https://www.tesourotransparente.gov.br/ckan/dataset/"
        "taxas-dos-titulos-ofertados-pelo-tesouro-direto\n"
        f"Encoding / separador {enc} / {sep!r}\n"
        f"Linhas lidas ....... {lidas}\n"
        f"Linhas no recorte .. {len(selecionadas)}\n"
        f"Selecoes geradas ... {len(escolhas)}\n",
        encoding="utf-8")

    print(f"\ngravados: {saida1.name}, {saida2.name}, {prov.name}")
    print(f"SHA-256 do original: {sha}")


if __name__ == "__main__":
    main()
