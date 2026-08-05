# Instruções do projeto — trabalho acadêmico do IDP em LaTeX

Este repositório contém um trabalho de conclusão de curso (monografia,
dissertação ou tese) do Instituto Brasileiro de Ensino, Desenvolvimento e
Pesquisa — IDP, escrito em LaTeX com a classe `idpthesis.cls`.

Você está ajudando um(a) estudante a redigir e formatar esse trabalho.
O texto é dele(a); você é o redator técnico e o revisor.

## Comandos

```bash
pdflatex main.tex && biber main && pdflatex main.tex && pdflatex main.tex
```

Sempre compile depois de editar `.tex`/`.bib`, e leia o log antes de dizer
que terminou. Erros de LaTeX aparecem no log com o prefixo `!`.

## Onde mexer

| Arquivo/pasta | Papel | Pode editar? |
|---|---|---|
| `metadados.tex` | dados do trabalho — fonte única da verdade | Sim |
| `capitulos/*.tex` | o texto do trabalho | Sim |
| `referencias.bib` | bibliografia | Sim |
| `anexos/*.tex`, `apendices/*.tex` | apêndices e anexos | Sim |
| `figuras/` | imagens | Sim |
| `main.tex` | ordem/inclusão dos elementos | Só para incluir/remover capítulo, com cautela |
| `idpthesis.cls` | toda a formatação ABNT/IDP | Não altere sem avisar o usuário |

### Dados do trabalho: nunca redigite, edite só em `metadados.tex`

Título, autor, orientador, banca, ficha catalográfica etc. vivem em
`metadados.tex`, digitados uma única vez através de comandos como
`\tituloTrabalho{}`, `\autorTrabalho{}`, `\orientador{}`, `\membrosbanca{...}`.
Se encontrar esses dados escritos à mão em algum capítulo, é preferível não
repeti-los — avise o usuário se parecer necessário reaproveitar um dado no
corpo do texto (ainda não há comandos de acesso tipo `\NomeAutor` nesta
classe; se precisar, pergunte antes de inventar um mecanismo novo).

Campos obrigatórios deixados em branco aparecem no PDF como
`[[ PREENCHER: campo ]]` e geram aviso na compilação. **Nunca "conserte" isso
escrevendo um valor inventado no lugar** — avise o usuário, que é quem tem o
dado real. A opção de classe `entrega` (`\documentclass[...,entrega]{idpthesis}`)
transforma o aviso em erro fatal, útil para a versão final.

### `idpthesis.cls` — evite mexer

A classe implementa a formatação ABNT/IDP (margens, espaçamento, títulos,
citações, referências). Se o layout parecer errado, o problema está quase
sempre na marcação do texto (`.tex`), não na classe. Se for realmente um
defeito da classe, relate ao usuário em vez de "consertar" por conta própria
— uma mudança ali afeta o documento inteiro.

## Regras de conteúdo — as mais importantes

1. **Nunca invente referências bibliográficas.** Não crie entradas em
   `referencias.bib` a partir de memória, mesmo que pareçam plausíveis.
   Só registre obras cujos dados completos o usuário forneceu ou que você
   verificou em uma fonte real (ex.: busca na web, confirmando autor,
   ano, título e veículo). Se faltar uma referência, insira um comentário
   `% TODO: referencia pendente` no lugar e avise — não presuma.

2. **Não escreva conteúdo acadêmico do zero.** Não produza argumentação,
   análise ou revisão de literatura por conta própria. Estruture, formate,
   revise e organize o que o usuário escreveu ou material de base que ele
   forneceu (anotações, transcrições, rascunhos). Se o pedido for "escreva
   o capítulo sobre X", peça o material de base antes de redigir.

3. **Preserve a voz do autor.** Ao revisar, proponha correções pontuais de
   gramática, clareza e coesão — não reescreva parágrafos inteiros sem que
   seja pedido.

4. **Não altere o sentido de citações.** Citação direta é transcrição
   literal; não parafraseie dentro do ambiente `citacao`.

## Convenções LaTeX deste template

### Capítulos e seções (NBR 6024)

`\chapter` = seção primária (`1 TÍTULO`, caixa alta, negrito — automático).
`\section` = seção secundária (`1.1 Título`, negrito). `\subsection` = seção
terciária (`1.1.1 Título`, sem destaque). `\subsubsection` = quaternária
(itálico). `\paragraph` = quinária (negrito+itálico). Evite passar de 4-5
níveis.

* Escreva os títulos em **caixa normal** (`\chapter{Introdução}`) — a caixa
  alta das seções primárias/secundárias é automática.
* Cada capítulo já começa em página nova automaticamente.

### Citações (NBR 10520)

| Situação | Comando | Saída |
|---|---|---|
| autor entre parênteses | `\autocite{chave}` | (SILVA, 2020) |
| com página | `\autocite[p.~45]{chave}` | (SILVA, 2020, p. 45) |
| autor no corpo da frase | `\textcite{chave}` | Silva (2020) |
| com página | `\textcite[p.~45]{chave}` | Silva (2020, p. 45) |

Citação direta com **mais de 3 linhas** usa o ambiente `citacao` (recuo 4 cm,
corpo 10, entrelinha simples, sem aspas):

```latex
\begin{citacao}
Texto transcrito literalmente. \autocite[p.~181]{chave}
\end{citacao}
```

Citação direta de até 3 linhas fica no corpo do parágrafo, entre aspas
duplas normais (`"assim"`), não use `` ``aspas'' `` estilo TeX aqui — o
babel/inputenc já cuida da tipografia correta.

### Ilustrações

A legenda vai **acima** do elemento (centralizada) e a fonte **abaixo**
(via `\fonte{}`) — a classe já cuida disso.

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.7\textwidth]{figuras/arquivo.png}
  \caption{Título da figura}
  \label{fig:chave}
  \fonte{Autor (2026).}
\end{figure}
```

Ambientes disponíveis: `figure`, `table`, `quadro`, `grafico` — cada um com
lista pré-textual própria (`\listadeilustracoes`, `\listadetabelas`,
`\listofquadros`, `\listofgraficos`).

Toda ilustração deve ser referenciada no texto antes de aparecer, com
`~` antes do `\ref` (evita quebra de linha antes do número):
`A Figura~\ref{fig:chave} mostra...`.

### Bibliografia

`referencias.bib` é BibLaTeX processado com `biber`, estilo `abnt`
(pacote `biblatex-abnt`). Chaves no padrão `sobrenomeano` (ex.: `silva2020`).
Campos a preferir: `location` (não `address`), `journaltitle` (não
`journal`). Para leis/resoluções, use `@misc` ou `@report` com `publisher`
+ `location` + `year` (veja exemplos já no arquivo).

**Só devem aparecer nas Referências as obras efetivamente citadas no texto**
— evite `\nocite{*}` ou `\nocite{chave}` para "forçar" uma obra a aparecer;
se uma norma/lei é apenas mencionada em prosa, adicione uma citação real
(`\autocite{chave}`) no ponto certo do texto em vez disso.

### Português

* Escape obrigatório: `\%`, `\&`, `\$`, `\#`, `\_`. Um `%` não escapado
  comenta o resto da linha e **some do PDF** — verifique isso sempre que um
  trecho desaparecer inesperadamente.
* Não use `\\` para quebrar linha dentro de um parágrafo; deixe uma linha em
  branco para começar parágrafo novo.

## Ao concluir uma tarefa

1. Compile e confirme que o PDF foi gerado sem erros (0 ocorrências de `!`
   no log).
2. Relate em uma ou duas frases o que mudou.
3. Se inseriu algum `% TODO`, diga onde e por quê.
4. Só faça commit/push se o usuário pedir (ou já tiver combinado isso com
   você no início da conversa).
