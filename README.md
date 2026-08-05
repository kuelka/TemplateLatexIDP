# TemplateLatexIDP

Template **não oficial** em LaTeX para monografias, dissertações e teses do
**IDP — Instituto Brasileiro de Ensino, Desenvolvimento e Pesquisa**, construído
a partir do modelo em Word publicado pela biblioteca do IDP:
<https://www.idp.edu.br/arquivos/biblioteca/templateMonografia_ou_TCC.pdf>

> Este repositório reconstrói fielmente a formatação do PDF acima (margens,
> fonte, espaçamento, estrutura pré-textual/textual/pós-textual e normas de
> citação/referência) em uma classe LaTeX reutilizável. Não é um material
> oficial do IDP — confira sempre o resultado com seu orientador e a
> secretaria acadêmica antes de entregar o trabalho.

## Estrutura do repositório

```
TemplateLatexIDP/
├── idpthesis.cls              # classe LaTeX com toda a formatação ABNT/IDP
├── main.tex                   # documento principal (edite os metadados aqui)
├── referencias.bib            # base de referências bibliográficas (BibLaTeX)
├── capitulos/
│   ├── 01-introducao.tex
│   ├── 02-referencial-teorico.tex
│   ├── 03-metodologia.tex
│   ├── 04-resultados.tex
│   └── 05-consideracoes-finais.tex
├── apendices/
│   └── apendice-a.tex
├── anexos/
│   └── anexo-a.tex
├── figuras/                   # coloque aqui suas imagens
├── .gitignore
├── README.md
└── TUTORIAL.md                 # como usar este template com Claude Code / Codex
```

## O que a classe `idpthesis.cls` já implementa

- Página A4, margens 3 cm (esquerda/superior) e 2 cm (direita/inferior) — NBR 14724.
- Fonte Times New Roman (via pacote `times`), corpo 12 pt.
- Espaçamento 1,5 no corpo do texto; espaçamento simples em resumo/abstract,
  citações diretas longas, notas de rodapé e referências.
- Recuo de parágrafo de 1,25 cm.
- Capa, folha de rosto, ficha catalográfica, folha de aprovação, dedicatória,
  agradecimentos, resumo, abstract, listas de ilustrações/tabelas/quadros/
  gráficos/abreviaturas e sumário — todos como comandos/ambientes prontos.
- Numeração de página no canto superior direito, visível apenas a partir da
  parte textual (Introdução), exatamente como no modelo do IDP.
- Títulos de capítulo em caixa alta e negrito, sem ponto após o número
  (NBR 6024); seções e subseções com hierarquia tipográfica decrescente.
- Ambiente `citacao` para citações diretas com mais de 3 linhas (recuo de
  4 cm, fonte 10, espaçamento simples, sem aspas) — NBR 10520.
- Referências bibliográficas automáticas com `biblatex` + `biber` no estilo
  `abnt` (pacote `biblatex-abnt`), sistema autor-data, ordenação alfabética —
  NBR 6023 e NBR 10520.
- Suporte a três tipos de trabalho via opção de classe:
  `\documentclass[monografia]{idpthesis}`, `[dissertacao]` ou `[tese]`.

## Dependências

- Uma distribuição LaTeX (TeX Live ≥ 2021 ou MiKTeX) com os pacotes:
  `geometry`, `times`, `babel` (com `brazilian`/`portuges`), `setspace`,
  `titlesec`, `tocloft`, `fancyhdr`, `caption`, `float`, `enumitem`,
  `scrextend`, `hyperref`, `biblatex` e `biblatex-abnt`.
- O motor de bibliografia **biber** (não use `bibtex` — o estilo `abnt` exige
  `biber`).

No Overleaf, tudo isso já vem pronto: basta enviar o projeto e escolher
"Biber" como bibliography backend nas configurações do projeto (menu
engrenagem → Bibliography → Biber). Em uma instalação local, veja o
`TUTORIAL.md` para o passo a passo de instalação.

## Como compilar localmente

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

(ou, se tiver `latexmk` instalado: `latexmk -pdf -bibtex-cond main.tex`)

## Licença

Uso livre para alunos e ex-alunos do IDP e demais interessados. Sem
garantias — sempre valide o resultado final com as normas vigentes do seu
programa e com a biblioteca do IDP (biblioteca@idp.edu.br).
