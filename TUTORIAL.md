# Tutorial: escrevendo sua monografia/dissertação/tese do IDP com este template

Este tutorial é para alunos do IDP que vão usar o **TemplateLatexIDP** para
escrever o trabalho de conclusão, e que pretendem contar com um assistente de
IA de linha de comando — **Claude Code** ou **Codex CLI** — para ajudar na
redação, formatação e correção do documento LaTeX.

Você não precisa saber LaTeX profundamente. O agente de IA consegue editar os
arquivos `.tex`, rodar a compilação e corrigir erros por você — mas é
importante que você entenda o essencial para revisar o que ele produz.

---

## 1. Visão geral do que você vai editar

Você **não precisa mexer** no arquivo `idpthesis.cls` (é a "engine" de
formatação). Os arquivos que você (ou o agente de IA, a seu pedido) vai editar
são:

| Arquivo | O que é |
|---|---|
| `metadados.tex` | Metadados do trabalho: título, autor, orientador, curso, banca, ficha catalográfica |
| `main.tex` | Estrutura do documento (resumo, abstract, dedicatória, agradecimentos, ordem dos capítulos) |
| `capitulos/01-introducao.tex` … `05-consideracoes-finais.tex` | O corpo do seu trabalho, um arquivo por capítulo |
| `referencias.bib` | Sua bibliografia (cada livro/artigo é uma entrada) |
| `apendices/*.tex`, `anexos/*.tex` | Apêndices e anexos, se houver |
| `figuras/` | Suas imagens (gráficos, prints, diagramas) |

---

## 2. Preparando o ambiente

### Opção A — Overleaf (mais simples, sem instalar nada)
1. Crie um projeto novo no Overleaf e envie todos os arquivos deste repositório
   (mantendo a estrutura de pastas).
2. No menu do projeto (ícone de engrenagem) → **Bibliography** → selecione
   **Biber**.
3. Compile normalmente com o botão "Recompile".

### Opção B — Sua máquina, com Claude Code ou Codex
1. Instale uma distribuição LaTeX completa (TeX Live no Linux/Mac, MiKTeX no
   Windows) e confirme que o comando `biber` está disponível
   (`biber --version`).
2. Clone este repositório.
3. Abra o terminal na pasta do projeto e inicie o Claude Code (`claude`) ou o
   Codex CLI (`codex`).

---

## 3. Fluxo de trabalho recomendado com o agente de IA

A estrutura em arquivos separados por capítulo existe **de propósito**: ela
permite que você peça ao agente para trabalhar em um capítulo de cada vez,
sem precisar que ele releia o trabalho inteiro a cada mudança, e permite que
você revise o `git diff` de cada capítulo isoladamente antes de aceitar.

Um fluxo que funciona bem:

1. **Preencha os metadados primeiro.** Peça ao agente para editar
   `metadados.tex` com o título, autor, orientador, curso e demais dados —
   é o único arquivo que concentra tudo isso, então nunca é preciso caçar
   texto solto pelo documento. Ajuste também a opção da classe em
   `main.tex` (`monografia`, `dissertacao` ou `tese`).
2. **Escreva/dite o conteúdo de um capítulo por vez.** Cole suas anotações,
   rascunhos ou até áudio transcrito, e peça para o agente estruturar aquele
   capítulo específico dentro do `.tex` correspondente.
3. **Peça para compilar depois de cada edição.** O agente deve rodar:
   ```bash
   pdflatex main.tex && biber main && pdflatex main.tex && pdflatex main.tex
   ```
   e ler o `.log`/a saída do terminal para corrigir erros de compilação antes
   de te devolver o resultado.
4. **Revise o PDF gerado** (visualmente ou extraindo o texto com
   `pdftotext -layout main.pdf -`) antes de pedir o próximo capítulo.
5. **Faça commits pequenos** (um por capítulo ou por sessão de edição), para
   poder desfazer facilmente se alguma edição do agente sair errada.

### Prompts de exemplo

Preenchendo os metadados:

> "Edite o `metadados.tex` deste projeto: sou aluno do curso de Direito,
> o trabalho é uma monografia, título 'A Responsabilidade Civil do Estado
> por Omissão', autor Fulano de Tal, orientador Prof. Dr. Sicrano de Souza.
> Troque a opção da classe em `main.tex` para `monografia`. Depois
> recompile e me confirme que não há erros."

Escrevendo um capítulo a partir de anotações suas:

> "No arquivo `capitulos/02-referencial-teorico.tex`, desenvolva a seção
> 2.1 (Responsabilidade objetiva do Estado) com base nestas anotações: [cole
> suas anotações ou rascunho aqui]. Use citação indireta sempre que
> parafrasear um autor, e o ambiente `citacao` para transcrições literais com
> mais de 3 linhas. Adicione as referências correspondentes em
> `referencias.bib` no formato BibLaTeX."

Corrigindo erros de compilação:

> "Rode a compilação completa (pdflatex, biber, pdflatex, pdflatex) e me
> mostre qualquer erro do `.log`. Se houver erro de LaTeX, corrija o arquivo
> `.tex` responsável e recompile até não haver mais erros."

Verificando a formatação ABNT:

> "Releia o capítulo 2 e verifique se todas as citações diretas com mais de 3
> linhas estão dentro do ambiente `citacao`, e se toda citação (direta ou
> indireta) tem uma entrada correspondente em `referencias.bib`. Aponte
> qualquer citação sem referência."

---

## 4. Como citar e referenciar (a parte que mais gera dúvida)

Este template usa **biblatex + biber**, sistema autor-data (igual ao exigido
pela NBR 10520). Você não escreve a referência manualmente no texto — você
cria uma entrada em `referencias.bib` e usa um comando de citação:

```bibtex
@book{silva2020,
  author    = {Silva, João da},
  title     = {Título do livro},
  year      = {2020},
  address   = {São Paulo},
  publisher = {Editora Exemplo}
}
```

E no capítulo:

```latex
De acordo com \textcite{silva2020}, ...
Outra afirmação relevante (\autocite{silva2020}).
Citação com página específica \autocite[p.~35]{silva2020}.
```

A lista de `REFERÊNCIAS` no final do documento é gerada **automaticamente**,
em ordem alfabética e no formato ABNT — você nunca precisa formatá-la à mão.

Peça ao agente de IA para popular o `.bib` conforme você for citando autores;
ele consegue fazer isso a partir do nome do livro/artigo, mas **sempre
confira manualmente se a referência existe de verdade e se os dados batem**
(ano, editora, página) — modelos de linguagem podem "inventar" referências
que parecem plausíveis, mas não existem.

---

## 5. Citações diretas curtas x longas (NBR 10520)

- **Até 3 linhas:** fica no corpo do parágrafo, entre aspas:
  ```latex
  Para o autor, "o direito é a arte do bom e do equitativo" \autocite[p.~10]{fulano2019}.
  ```
- **Mais de 3 linhas:** use o ambiente `citacao` (recuo de 4 cm, fonte menor,
  espaçamento simples, sem aspas):
  ```latex
  \begin{citacao}
  Texto longo transcrito literalmente do autor consultado, mantendo a
  redação original...  \autocite[p.~181]{fulano2019}
  \end{citacao}
  ```

---

## 6. Inserindo figuras, tabelas e gráficos

Toda ilustração exige a fonte (mesmo que seja "Do autor"):

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.7\textwidth]{figuras/meu-grafico.png}
  \caption{Evolução do indicador X}
  \label{fig:indicador-x}
  \fonte{Do autor (2026).}
\end{figure}
```

---

## 7. Checklist antes de entregar

- [ ] Todos os campos de `metadados.tex` preenchidos (título, autor,
      orientador, matrícula, banca examinadora) e o resumo/abstract em
      `main.tex`.
- [ ] Ficha catalográfica solicitada à Biblioteca Ministro Moreira Alves
      (biblioteca@idp.edu.br) e colada em `metadados.tex` via
      `\fichacatalograficatexto{...}`.
- [ ] Todas as citações diretas e indiretas têm entrada em `referencias.bib`
      e as referências existem de fato (confira manualmente).
- [ ] Compilação sem erros: `pdflatex` → `biber` → `pdflatex` → `pdflatex`.
- [ ] PDF final revisado por você (e, se possível, pelo orientador) —
      formatação automática não substitui revisão humana.
- [ ] Confirme com a secretaria/orientador que não houve mudança recente no
      modelo oficial do IDP que este template ainda não contemple.
- [ ] Se sua instituição exigir declaração de uso de IA na redação, inclua-a
      conforme a política vigente do seu curso.

---

## 8. Nota sobre uso responsável de IA

Usar Claude Code ou Codex para agilizar a formatação, organizar referências e
revisar a estrutura do texto é legítimo e produtivo. Mas o conteúdo
intelectual do trabalho — a análise, os argumentos, as conclusões — precisa
ser seu. Trate o agente como um assistente de editoração e revisão, não como
autor do conteúdo acadêmico, e sempre verifique manualmente qualquer citação,
dado ou referência que ele sugerir.
