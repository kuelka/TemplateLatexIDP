%% idpthesis.cls
%% ---------------------------------------------------------------------
%% Classe LaTeX nao-oficial para monografias, dissertacoes e teses do
%% Instituto Brasileiro de Ensino, Desenvolvimento e Pesquisa - IDP.
%%
%% Replica a formatacao do template oficial em Word disponibilizado em:
%% https://www.idp.edu.br/arquivos/biblioteca/templateMonografia_ou_TCC.pdf
%%
%% Segue as normas da ABNT vigentes referenciadas no proprio template:
%%   NBR 14724:2011 - Trabalhos academicos - Apresentacao
%%   NBR 6027:2012  - Sumario
%%   NBR 6024:2012  - Numeracao progressiva das secoes
%%   NBR 6028:2021  - Resumo
%%   NBR 10520:2002 - Citacoes em documentos
%%   NBR 6023:2018  - Referencias
%%
%% Este arquivo NAO e um produto oficial do IDP. E uma reconstrucao de
%% formatacao feita a partir do PDF de exemplo publicado pela instituicao.
%% Sempre confira o resultado final com a secretaria/orientador antes de
%% entregar o trabalho.
%% ---------------------------------------------------------------------

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{idpthesis}[2026/08/05 v1.0 Classe nao-oficial IDP (monografia/dissertacao/tese)]

%% =======================================================================
%% 1. OPCOES DE CLASSE
%% =======================================================================
\newif\ifidp@monografia  \idp@monografiafalse
\newif\ifidp@dissertacao \idp@dissertacaofalse
\newif\ifidp@tese        \idp@tesefalse
%% Opcao 'entrega': transforma em erro fatal (interrompe a compilacao) o
%% aviso de campo obrigatorio nao preenchido em metadados.tex. Use ao gerar
%% a versao final, para nao correr o risco de entregar um PDF com
%% "[[ PREENCHER: ... ]]" esquecido no meio do texto.
\newif\ifidp@entrega     \idp@entregafalse

\DeclareOption{monografia}{\idp@monografiatrue}
\DeclareOption{dissertacao}{\idp@dissertacaotrue}
\DeclareOption{tese}{\idp@tesetrue}
\DeclareOption{entrega}{\idp@entregatrue}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}

\ExecuteOptions{monografia}
\ProcessOptions\relax

\ifidp@monografia\else\ifidp@dissertacao\else\ifidp@tese\else
  \idp@monografiatrue
\fi\fi\fi

\LoadClass[12pt,a4paper,oneside]{report}

%% =======================================================================
%% 2. PACOTES BASE E IDIOMA
%% =======================================================================
\RequirePackage[T1]{fontenc}
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage[utf8]{inputenc}
\RequirePackage[brazil]{babel}
\RequirePackage{microtype}               % melhora justificacao/quebra de linha
\frenchspacing                            % pt-BR: sem espaco extra apos ponto final
\RequirePackage{times}
\RequirePackage{xcolor}
\RequirePackage{graphicx}
\RequirePackage{xparse}
\RequirePackage{etoolbox}
\RequirePackage{ifthen}
\RequirePackage{lastpage}

%% -----------------------------------------------------------------------
%% 3. GEOMETRIA DA PAGINA - NBR 14724, secao 5.1
%% -----------------------------------------------------------------------
\RequirePackage[a4paper,top=3cm,left=3cm,right=2cm,bottom=2cm]{geometry}

%% -----------------------------------------------------------------------
%% 4. ESPACAMENTO E PARAGRAFOS
%% -----------------------------------------------------------------------
\RequirePackage{setspace}
\onehalfspacing
\RequirePackage{indentfirst}
\setlength{\parindent}{1.25cm}
\setlength{\parskip}{0pt}

%% -----------------------------------------------------------------------
%% 5. NUMERACAO DE PAGINA - NBR 14724, secao 5.3
%% -----------------------------------------------------------------------
\RequirePackage{fancyhdr}
\setlength{\headheight}{14.5pt}
%% Redefine tambem o estilo "plain" (usado internamente por \chapter em
%% cada abertura de capitulo) para manter a numeracao sempre no canto
%% superior direito, conforme a NBR 14724.
\fancypagestyle{idpcomnumero}{%
  \fancyhf{}%
  \fancyhead[R]{\thepage}%
  \renewcommand{\headrulewidth}{0pt}%
}
\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyhead[R]{\thepage}%
  \renewcommand{\headrulewidth}{0pt}%
}
\pagestyle{empty}

%% Controla se ja estamos na parte textual (a partir da Introducao). Antes
%% disso, mesmo as paginas que abrem "capitulo" (Lista de ilustracoes,
%% Sumario etc.) devem permanecer sem numero visivel.
\newif\ifidptextual \idptextualfalse

\newcommand{\idpiniciotextual}{%
  \cleardoublepage
  \idptextualtrue
  \pagestyle{idpcomnumero}%
}

%% -----------------------------------------------------------------------
%% 6. TITULOS DE SECAO - NBR 6024
%% -----------------------------------------------------------------------
\RequirePackage{titlesec}
\RequirePackage{titletoc}

\titleformat{\chapter}[hang]
  {\normalfont\bfseries\Large}
  {\MakeUppercase{\thechapter}}
  {1em}
  {\MakeUppercase}
\titlespacing*{\chapter}{0pt}{0pt}{\baselineskip}

\titleformat{\section}
  {\normalfont\bfseries\large}
  {\thesection}
  {1em}
  {}
\titlespacing*{\section}{0pt}{\baselineskip}{0.5\baselineskip}

%% NBR 6024 - hierarquia tipografica progressiva (convencao mais usual,
%% adotada por exemplo pelo abnTeX2): 1o nivel CAIXA ALTA+negrito (chapter,
%% acima); 2o nivel negrito (section, acima); 3o nivel sem destaque
%% (subsection); 4o nivel italico (subsubsection); 5o nivel negrito+italico
%% (paragraph). Nao use mais de 5 niveis de secao.
\titleformat{\subsection}
  {\normalfont\normalsize}
  {\thesubsection}
  {1em}
  {}
\titlespacing*{\subsection}{0pt}{0.5\baselineskip}{0.25\baselineskip}

\titleformat{\subsubsection}
  {\normalfont\itshape\normalsize}
  {\thesubsubsection}
  {1em}
  {}
\titlespacing*{\subsubsection}{0pt}{0.5\baselineskip}{0.25\baselineskip}

\titleformat{\paragraph}
  {\normalfont\bfseries\itshape\normalsize}
  {\theparagraph}
  {1em}
  {}
\titlespacing*{\paragraph}{0pt}{0.5\baselineskip}{0.25\baselineskip}

\setcounter{secnumdepth}{4}
\setcounter{tocdepth}{3}

\newcommand{\idpcapitulosemnumero}[1]{%
  \chapter*{\MakeUppercase{#1}}
  \addcontentsline{toc}{chapter}{\MakeUppercase{#1}}
  \ifidptextual\else\thispagestyle{empty}\fi
}

%% -----------------------------------------------------------------------
%% 7. SUMARIO - NBR 6027
%% -----------------------------------------------------------------------
\RequirePackage{tocloft}
\renewcommand{\cftchapfont}{\bfseries}
\renewcommand{\cftchappagefont}{\bfseries}
\setlength{\cftbeforechapskip}{0.5\baselineskip}
\renewcommand{\cftchappresnum}{}
\renewcommand{\cftchapaftersnum}{}
\setlength{\cftchapnumwidth}{2.2em}
\setlength{\cftsecindent}{2.2em}
\setlength{\cftsecnumwidth}{2.4em}
\setlength{\cftsubsecindent}{4.6em}
\setlength{\cftsubsecnumwidth}{2.8em}
\renewcommand{\contentsname}{SUM\'ARIO}

%% -----------------------------------------------------------------------
%% 8. LEGENDAS DE FIGURAS/TABELAS/QUADROS/GRAFICOS
%% -----------------------------------------------------------------------
%% NBR 14724 (praxe consolidada nos manuais de ilustracoes da ABNT): o
%% titulo/legenda fica ACIMA da ilustracao, centralizado; a fonte fica
%% ABAIXO. position=top garante isso para figure/table e para os floats
%% customizados (quadro/grafico) definidos logo abaixo.
\RequirePackage[
  format=plain,
  labelsep=endash,
  font=small,
  labelfont=bf,
  justification=centering,
  singlelinecheck=false,
  position=top
]{caption}

\RequirePackage{float}
\RequirePackage{booktabs}
\RequirePackage{tabularx}
\RequirePackage{adjustbox}
\RequirePackage{longtable}
\floatstyle{plaintop}
\newfloat{quadro}{tbp}{loq}[chapter]
\floatname{quadro}{Quadro}
\newfloat{grafico}{tbp}{logr}[chapter]
\floatname{grafico}{Gr\'afico}
\captionsetup[figure]{position=top}
\captionsetup[table]{position=top}
\captionsetup[quadro]{position=top}
\captionsetup[grafico]{position=top}

\newcommand{\listofquadros}{%
  \idpcapitulosemnumero{Lista de Quadros}
  \listof{quadro}{}
}
\newcommand{\listofgraficos}{%
  \idpcapitulosemnumero{Lista de Gr\'aficos}
  \listof{grafico}{}
}

\newcommand{\fonte}[1]{%
  \par\vspace{2pt}
  {\centering\small\textbf{Fonte:}~#1\par}
}
\newcommand{\nota}[1]{%
  \par\vspace{2pt}
  {\centering\small\textbf{Nota:}~#1\par}
}

%% -----------------------------------------------------------------------
%% 9. CITACOES - NBR 10520
%% -----------------------------------------------------------------------
\RequirePackage{scrextend}
\newenvironment{citacao}{%
  \begin{addmargin}[4cm]{0cm}%
  \singlespacing\fontsize{10}{12}\selectfont
  \setlength{\parindent}{0pt}%
}{%
  \end{addmargin}
  \par\vspace{\baselineskip}
}

%% -----------------------------------------------------------------------
%% 10. NOTAS DE RODAPE
%% -----------------------------------------------------------------------
\renewcommand{\footnotesize}{\fontsize{10}{12}\selectfont}

%% =======================================================================
%% 11. METADADOS DO TRABALHO
%% =======================================================================
%% Auxilia a preencher "[XX] f." na ficha catalografica sem precisar
%% contar paginas manualmente: use \numerodepaginas dentro do texto
%% passado a \fichacatalograficatexto (requer 2 compilacoes para atualizar).
\newcommand{\numerodepaginas}{\pageref{LastPage}}

\newcommand{\instituicao}[1]{\def\idpinstituicao{#1}}
\instituicao{Instituto Brasileiro de Ensino, Desenvolvimento e Pesquisa -- IDP}

\newcommand{\campus}[1]{\def\idpcampus{#1}}
\campus{Bras\'ilia-DF}

\newcommand{\curso}[1]{\def\idpcurso{#1}}
\newcommand{\programapos}[1]{\def\idpprogramapos{#1}}
\newcommand{\areaconcentracao}[1]{\def\idpareaconcentracao{#1}}
\newcommand{\linhapesquisa}[1]{\def\idplinhapesquisa{#1}}
\let\idplinhapesquisa\@empty

%% Numero de matricula do aluno (opcional; aparece na folha de
%% aprovacao se preenchido). Comum em dissertacoes/teses de
%% mestrado/doutorado, dispensavel em monografias de graduacao.
\newcommand{\matricula}[1]{\def\idpmatricula{#1}}
\let\idpmatricula\@empty

%% -----------------------------------------------------------------------
%% Marcador de campo obrigatorio nao preenchido: aparece em destaque no
%% PDF (para ser impossivel de ignorar na revisao final) e dispara aviso
%% na compilacao. Com a opcao de classe 'entrega', vira erro fatal.
%% -----------------------------------------------------------------------
\newcommand{\idpcampovazio}[1]{[[ PREENCHER: #1 ]]}
\newcount\idppendentes
\newcommand{\idpconfere}[2]{%
  \def\idptmp{\idpcampovazio{#1}}%
  \ifx#2\idptmp
    \global\advance\idppendentes by 1\relax
    \ClassWarningNoLine{idpthesis}{Campo obrigatorio nao preenchido: #1}%
  \fi
}

\newcommand{\tituloTrabalho}[1]{\def\idptitulo{#1}}
\def\idptitulo{\idpcampovazio{titulo}}
\newcommand{\subtituloTrabalho}[1]{\def\idpsubtitulo{#1}}
\let\idpsubtitulo\@empty

\newcommand{\autorTrabalho}[1]{\def\idpautor{#1}}
\def\idpautor{\idpcampovazio{autor}}

\newcommand{\orientador}[1]{\def\idporientador{#1}}
\def\idporientador{\idpcampovazio{orientador}}
\newcommand{\coorientador}[1]{\def\idpcoorientador{#1}}
\let\idpcoorientador\@empty

\newcommand{\localdefesa}[1]{\def\idplocal{#1}}
\localdefesa{Bras\'ilia-DF}

\newcommand{\anotrabalho}[1]{\def\idpano{#1}}
\anotrabalho{\the\year}

\newcommand{\datadefesa}[1]{\def\idpdatadefesa{#1}}
\def\idpdatadefesa{\idpcampovazio{datadefesa}}

\newcommand{\membrosbanca}[1]{\def\idpbanca{#1}}

%% Verificacao dos campos obrigatorios (roda apos metadados.tex/main.tex
%% terem sido lidos, ja no inicio do documento).
\AtBeginDocument{%
  \idpconfere{titulo}{\idptitulo}%
  \idpconfere{autor}{\idpautor}%
  \idpconfere{orientador}{\idporientador}%
  \idpconfere{datadefesa}{\idpdatadefesa}%
  \ifnum\idppendentes>0\relax
    \ifidp@entrega
      \ClassError{idpthesis}{%
        \the\idppendentes\space campo(s) obrigatorio(s) nao preenchido(s) em
        metadados.tex}{%
        Procure por "[[ PREENCHER" no PDF e pelas linhas "Campo obrigatorio
        nao preenchido" acima neste log. Preencha metadados.tex ou remova a
        opcao 'entrega' da classe para gerar um PDF de rascunho mesmo
        assim.}%
      \stop
    \else
      \ClassWarningNoLine{idpthesis}{%
        ATENCAO: \the\idppendentes\space campo(s) de metadados.tex ainda
        nao preenchido(s). Eles aparecem como "[[ PREENCHER: ... ]]" no PDF.
        Use a opcao de classe 'entrega' para transformar isto em erro antes
        de gerar a versao final}%
    \fi
  \fi
}

\newcommand{\fichacatalograficatexto}[1]{\def\idpficha{#1}}
\let\idpficha\@empty

\newcommand{\naturezatrabalho}[1]{\def\idpnatureza{#1}}
\let\idpnatureza\@empty

%% =======================================================================
%% 12. ELEMENTOS PRE-TEXTUAIS
%% =======================================================================

\newcommand{\capa}{%
  \clearpage
  \thispagestyle{empty}
  \begin{center}
    \MakeUppercase{\idpinstituicao}\\[2\baselineskip]
    \ifdef{\idpcurso}{\idpcurso\\}{}
    \vspace*{4cm}
    {\bfseries\MakeUppercase{\idptitulo}}\\
    \ifx\idpsubtitulo\@empty\else \idpsubtitulo\\\fi
    \vspace{2cm}
    \idpautor
    \vfill
    \idplocal\\
    \idpano
  \end{center}
  \clearpage
}

\newcommand{\idptextonatureza}{%
  \ifx\idpnatureza\@empty
    \ifidp@monografia
      Monografia apresentada como requisito para obten\c{c}\~ao do t\'itulo
      de bacharel em \idpcurso\ do \idpinstituicao.
    \fi
    \ifidp@dissertacao
      Disserta\c{c}\~ao apresentada ao Programa de P\'os-Gradua\c{c}\~ao em
      \idpprogramapos, como parte do requisito para a obten\c{c}\~ao do
      t\'itulo de Mestre em \idpareaconcentracao\ pelo \idpinstituicao.
    \fi
    \ifidp@tese
      Tese apresentada ao Programa de P\'os-Gradua\c{c}\~ao em
      \idpprogramapos, como parte do requisito para a obten\c{c}\~ao do
      t\'itulo de Doutor em \idpareaconcentracao\ pelo \idpinstituicao.
    \fi
  \else
    \idpnatureza
  \fi
}

\newcommand{\folioderosto}{%
  \clearpage
  \thispagestyle{empty}
  \begin{center}
    {\bfseries\MakeUppercase{\idpautor}}\\[3\baselineskip]
    {\bfseries\MakeUppercase{\idptitulo}}\\
    \ifx\idpsubtitulo\@empty\else \idpsubtitulo\\\fi
  \end{center}
  \vspace{2cm}
  \begin{flushright}
    \begin{minipage}{8cm}
      \singlespacing\fontsize{12}{14}\selectfont
      \idptextonatureza\par\vspace{\baselineskip}
      Orientador(a): \idporientador
      \ifx\idpcoorientador\@empty\else\par\vspace{.5\baselineskip}Coorientador(a): \idpcoorientador\fi
    \end{minipage}
  \end{flushright}
  \vfill
  \begin{center}
    \idplocal\\
    \idpano
  \end{center}
  \clearpage
}

\newcommand{\fichacatalografica}{%
  \clearpage
  \thispagestyle{empty}
  \vspace*{\fill}
  \noindent\rule{\linewidth}{0.4pt}\par\vspace{2pt}
  \begin{footnotesize}
    \ifx\idpficha\@empty
      \textit{[Cole aqui o texto da ficha catalogr\'afica fornecido pela
      Biblioteca Ministro Moreira Alves. Solicite em
      biblioteca@idp.edu.br.]}
    \else
      \idpficha
    \fi
  \end{footnotesize}
  \vspace{2pt}\noindent\rule{\linewidth}{0.4pt}
  \vspace*{\fill}
  \clearpage
}

\newcommand{\folhadeaprovacao}{%
  \clearpage
  \thispagestyle{empty}
  \begin{center}
    {\bfseries\MakeUppercase{\idpautor}}\\
    \ifx\idpmatricula\@empty\else Matr\'icula: \idpmatricula\\\fi
    \vspace{1\baselineskip}
    {\bfseries\MakeUppercase{\idptitulo}}\\
    \ifx\idpsubtitulo\@empty\else \idpsubtitulo\\\fi
    \vspace{1.5cm}
    \begin{minipage}{10cm}
      \idptextonatureza
    \end{minipage}
    \vspace{1cm}\\
    \idplocal, \idpdatadefesa
    \vspace{2cm}\\
    \textbf{Banca Examinadora}
    \vspace{1cm}\\
  \end{center}
  \idpbanca
  \clearpage
}
\newcommand{\examinador}[2]{%
  \par\vspace{2\baselineskip}
  \noindent\hfil\begin{minipage}{8cm}\centering
    \makebox[8cm]{\hrulefill}\\
    #1\\
    #2
  \end{minipage}\hfil\par
}

\newenvironment{dedicatoria}{%
  \clearpage
  \thispagestyle{empty}
  \null\vfill
  \begin{flushright}
  \begin{minipage}{8cm}
  \raggedleft
}{%
  \end{minipage}
  \end{flushright}
  \clearpage
}

\newenvironment{agradecimentos}{%
  \clearpage
  \thispagestyle{empty}
  \begin{center}\bfseries AGRADECIMENTOS\end{center}
  \vspace{\baselineskip}
}{%
  \clearpage
}

\newenvironment{resumo}[1]{%
  \clearpage
  \thispagestyle{empty}
  \begin{center}\bfseries RESUMO\end{center}
  \vspace{\baselineskip}
  \singlespacing\fontsize{12}{14}\selectfont
  \setlength{\parindent}{1.25cm}
  \def\idppalavraschave{#1}
}{%
  \par\vspace{2\baselineskip}
  \noindent\textbf{Palavras-chave:} \idppalavraschave
  \clearpage
}

\newenvironment{resumoingles}[1]{%
  \clearpage
  \thispagestyle{empty}
  \begin{center}\bfseries ABSTRACT\end{center}
  \vspace{\baselineskip}
  \singlespacing\fontsize{10}{12}\selectfont
  \setlength{\parindent}{1.25cm}
  \def\idpkeywords{#1}
}{%
  \par\vspace{2\baselineskip}
  \noindent\textbf{Keywords:} \idpkeywords
  \clearpage
}

\renewcommand{\listfigurename}{Lista de Ilustra\c{c}\~oes}
\renewcommand{\listtablename}{Lista de Tabelas}

\makeatletter
\newcommand{\listadeilustracoes}{%
  \idpcapitulosemnumero{Lista de Ilustra\c{c}\~oes}
  \@starttoc{lof}%
}
\newcommand{\listadetabelas}{%
  \idpcapitulosemnumero{Lista de Tabelas}
  \@starttoc{lot}%
}
\makeatother

\RequirePackage{enumitem}
\newenvironment{listadeabreviaturas}{%
  \idpcapitulosemnumero{Lista de Abreviaturas e Siglas}
  \begin{description}[labelwidth=2.5cm,leftmargin=3.5cm,style=multiline]
}{%
  \end{description}
}
\newcommand{\sigla}[2]{\item[#1] #2}

\makeatletter
\newcommand{\sumario}{%
  \idpcapitulosemnumero{Sum\'ario}
  \@starttoc{toc}%
}
\makeatother

%% =======================================================================
%% 13. REFERENCIAS BIBLIOGRAFICAS - NBR 6023 / NBR 10520
%% =======================================================================
\RequirePackage[
  style=abnt,
  language=brazil,
  backend=biber,
  uniquename=init,
  giveninits=true
]{biblatex}

\newcommand{\referencias}{%
  \idpcapitulosemnumero{Refer\^encias}
  \begingroup
  \singlespacing
  \printbibliography[heading=none]
  \endgroup
}

%% =======================================================================
%% 14. APENDICES E ANEXOS - NBR 14724, secao 6
%% =======================================================================
\newcommand{\apendices}{%
  \idpcapitulosemnumero{Ap\^endices}
}
\newcommand{\anexos}{%
  \idpcapitulosemnumero{Anexos}
}
\newcounter{idpapendice}
\renewcommand{\theidpapendice}{\Alph{idpapendice}}
\newcommand{\apendice}[1]{%
  \refstepcounter{idpapendice}
  \chapter*{AP\^ENDICE~\theidpapendice~-- #1}
  \addcontentsline{toc}{chapter}{AP\^ENDICE~\theidpapendice~-- #1}
}
\newcounter{idpanexo}
%% Padrao: letras (A, B, C...). Se o seu trabalho usa numeros romanos
%% (ANEXO I, II, III...), sobrescreva no seu main.tex, apos o \documentclass:
%%   \renewcommand{\theidpanexo}{\Roman{idpanexo}}
\renewcommand{\theidpanexo}{\Alph{idpanexo}}
\newcommand{\anexo}[1]{%
  \refstepcounter{idpanexo}
  \chapter*{ANEXO~\theidpanexo~-- #1}
  \addcontentsline{toc}{chapter}{ANEXO~\theidpanexo~-- #1}
}

%% =======================================================================
%% 15. HYPERLINKS
%% =======================================================================
\RequirePackage[hidelinks]{hyperref}

%% Evita erro do \MakeUppercase dentro de marcadores do PDF (bookmarks)
\pdfstringdefDisableCommands{%
  \let\MakeUppercase\relax
}


\endinput
