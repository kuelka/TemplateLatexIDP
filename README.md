# TemplateLatexIDP

![Compilar o PDF](https://github.com/kuelka/TemplateLatexIDP/actions/workflows/build.yml/badge.svg)

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
├── main.tex                   # documento principal (estrutura do trabalho)
├── metadados.tex              # TODOS os dados do trabalho: título, autor,
│                               # orientador, banca, ficha catalográfica etc.
│                               # -- é o único arquivo que você deveria
│                               # precisar editar para "preencher os campos"
├── referencias.bib            # base de referências bibliográficas (BibLaTeX)
├── capitulos/
│   ├── 01-introducao.tex
│   ├── 02-referencial-teorico.tex
│   ├── 03-hipoteses.tex
│   ├── 04-metodologia.tex
│   ├── 05-resultados.tex
│   ├── 06-discussao.tex
│   └── 07-conclusao.tex
├── anexos/
│   ├── anexo-1-cronograma.tex
│   ├── anexo-2-personas.tex
│   ├── anexo-3-instrumento-avaliacao.tex
│   └── anexo-4-questionario-sus.tex
├── apendices/
│   └── apendice-a.tex          # exemplo -- este trabalho não usa apêndices
├── figuras/                    # coloque aqui suas imagens
├── .gitignore
├── README.md
└── TUTORIAL.md                 # como usar este template com Claude Code / Codex
```

## Como preencher os dados do trabalho (substituindo os "placeholders em vermelho" do template Word)

O template oficial em Word marca em vermelho os trechos que cada aluno deve
substituir (nome do curso, título, orientador, ano etc.). Aqui isso é
resolvido de um jeito mais seguro que ficar caçando texto solto no
documento: **cada dado tem seu próprio comando ("variável"), definido uma
única vez em `metadados.tex` e usado automaticamente em todos os lugares
certos** (capa, folha de rosto, ficha catalográfica, folha de aprovação).

Não é necessário (nem recomendado) criar um arquivo de texto solto e um
parser para lê-lo — o próprio LaTeX já funciona como esse "banco de
variáveis": `\comando{valor}` É a variável. Colocar todos esses comandos em
um arquivo `metadados.tex` separado, importado por `\input{metadados}` no
topo do `main.tex`, dá exatamente o benefício que se busca (um lugar único
para editar, reaproveitável, fácil de dar diff no git) sem reinventar um
mecanismo de parsing.

Tabela de referência com todas as variáveis disponíveis na classe:

| Comando | Onde aparece | Obrigatório? |
|---|---|---|
| `\instituicao{}` | Capa, folha de rosto | Sim (já vem preenchido com o nome do IDP) |
| `\curso{}` | Capa (linha abaixo da instituição) | Recomendado |
| `\programapos{}` | Texto de natureza do trabalho (dissertação/tese) | Para dissertação/tese |
| `reaconcentracao{}` | Texto de natureza do trabalho (dissertação/tese) | Para dissertação/tese |
| `\linhapesquisa{}` | Reservado para uso manual (ex.: dentro de `
aturezatrabalho`) | Opcional |
| `	ituloTrabalho{}` | Capa, folha de rosto, folha de aprovação, ficha catalográfica | Sim |
| `\subtituloTrabalho{}` | Capa, folha de rosto, folha de aprovação | Opcional |
| `utorTrabalho{}` | Capa, folha de rosto, folha de aprovação | Sim |
| `\matricula{}` | Folha de aprovação (abaixo do nome do autor) | Opcional |
| `\orientador{}` | Folha de rosto, ficha catalográfica, banca | Sim |
| `\coorientador{}` | Folha de rosto | Opcional |
| `\membrosbanca{...}` com `\examinador{Nome}{Papel}` | Folha de aprovação | Sim |
| `\localdefesa{}` | Capa, folha de rosto, folha de aprovação | Sim (já vem "Brasília-DF") |
| `notrabalho{}` | Capa, folha de rosto | Sim |
| `\datadefesa{}` | Folha de aprovação | Sim |
| `
aturezatrabalho{}` | Folha de rosto, folha de aprovação | Opcional (senão, é gerado automaticamente a partir do tipo de trabalho + `\programapos`/`reaconcentracao`) |
| `ichacatalograficatexto{}` | Página da ficha catalográfica | Sim (peça o texto oficial à Biblioteca Ministro Moreira Alves) |
| `
umerodepaginas` | Use dentro do texto da ficha catalográfica no lugar de "XX f." | Opcional, mas recomendado (preenche sozinho, via pacote `lastpage`) |

Fluxo recomendado para começar um trabalho novo:

1. Copie `main.tex` e `metadados.tex` como ponto de partida.
2. Preencha **apenas** o `metadados.tex`.
3. Troque a opção da classe em `main.tex` (`monografia`, `dissertacao` ou
   `tese`) conforme o seu caso.
4. Se seu trabalho usa apêndices/anexos numerados com letras (padrão A, B,
   C — o default da classe) mantenha como está; se usar números romanos
   (I, II, III — comum em programas de mestrado/doutorado), adicione logo
   após o `\documentclass`:
   ```latex
   
enewcommand{	heidpanexo}{\Roman{idpanexo}}
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
- Legendas de figuras/tabelas/quadros/gráficos **acima** do elemento e
  "Fonte:" **abaixo**, centralizadas — conforme a praxe da ABNT.
- Opção de classe `entrega`: transforma em erro fatal qualquer campo
  obrigatório de `metadados.tex` deixado em branco (evita gerar a versão
  final com um `[[ PREENCHER: ... ]]` esquecido no meio do texto).
- Compilação automática via GitHub Actions a cada push (veja o badge no
  topo deste README) — o PDF fica disponível como artefato na aba
  *Actions*, mesmo que você não tenha LaTeX instalado.
- `AGENTS.md`/`CLAUDE.md`: instruções para agentes de IA (Claude Code,
  Codex) sobre como editar este repositório com segurança.

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
latexmk -pdf main.tex
```

(o `latexmkrc` deste repositório já configura o `biber` e roda as passagens
necessárias na ordem certa. Sem `latexmk`, o equivalente manual é:)

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

Não tem LaTeX instalado? Não é obrigatório: a cada push para o `main`, o
GitHub Actions compila o PDF automaticamente (veja a aba *Actions* do
repositório) e o disponibiliza como artefato para download.

Para gerar a versão final com validação estrita (aborta a compilação
se algum campo obrigatório de `metadados.tex` ainda estiver em branco),
adicione `entrega` às opções da classe em `main.tex`:

```latex
\documentclass[dissertacao,entrega]{idpthesis}
```

e recompile. Remova a opção para voltar a compilar rascunhos normalmente.

## Licença

Uso livre para alunos e ex-alunos do IDP e demais interessados. Sem
garantias — sempre valide o resultado final com as normas vigentes do seu
programa e com a biblioteca do IDP (biblioteca@idp.edu.br).
