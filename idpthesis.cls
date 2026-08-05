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

\DeclareOption{monografia}{\idp@monografiatrue}
\DeclareOption{dissertacao}{\idp@dissertacaotrue}
\DeclareOption{tese}{\idp@tesetrue}

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
\RequirePackage[utf8]{inputenc}
\RequirePackage[brazil]{babel}
\RequirePackage{times}
\RequirePackage{xcolor}
\RequirePackage{graphicx}
\RequirePackage{xparse}
\RequirePackage{etoolbox}
\RequirePackage{ifthen}

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

\titleformat{\subsection}
  {\normalfont\itshape\normalsize}
  {\thesubsection}
  {1em}
  {}
\titlespacing*{\subsection}{0pt}{0.5\baselineskip}{0.25\baselineskip}

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
\RequirePackage[
  format=plain,
  labelsep=endash,
  font=small,
  labelfont=bf,
  justification=raggedright,
  singlelinecheck=false
]{caption}

\RequirePackage{float}
\newfloat{quadro}{tbp}{loq}[chapter]
\floatname{quadro}{Quadro}
\newfloat{grafico}{tbp}{logr}[chapter]
\floatname{grafico}{Gr\'afico}

\newcommand{\listofquadros}{%
  \idpcapitulosemnumero{Lista de Quadros}
  \listof{quadro}{}
}
\newcommand{\listofgraficos}{%
  \idpcapitulosemnumero{Lista de Gr\'aficos}
  \listof{grafico}{}
}

\newcommand{\fonte}[1]{%
  {\small\raggedright Fonte: #1\par}
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
\newcommand{\instituicao}[1]{\def\idpinstituicao{#1}}
\instituicao{Instituto Brasileiro de Ensino, Desenvolvimento e Pesquisa -- IDP}

\newcommand{\campus}[1]{\def\idpcampus{#1}}
\campus{Bras\'ilia-DF}

\newcommand{\curso}[1]{\def\idpcurso{#1}}
\newcommand{\programapos}[1]{\def\idpprogramapos{#1}}
\newcommand{\areaconcentracao}[1]{\def\idpareaconcentracao{#1}}

\newcommand{\tituloTrabalho}[1]{\def\idptitulo{#1}}
\newcommand{\subtituloTrabalho}[1]{\def\idpsubtitulo{#1}}
\let\idpsubtitulo\@empty

\newcommand{\autorTrabalho}[1]{\def\idpautor{#1}}

\newcommand{\orientador}[1]{\def\idporientador{#1}}
\newcommand{\coorientador}[1]{\def\idpcoorientador{#1}}
\let\idpcoorientador\@empty

\newcommand{\localdefesa}[1]{\def\idplocal{#1}}
\localdefesa{Bras\'ilia-DF}

\newcommand{\anotrabalho}[1]{\def\idpano{#1}}
\anotrabalho{\the\year}

\newcommand{\datadefesa}[1]{\def\idpdatadefesa{#1}}

\newcommand{\membrosbanca}[1]{\def\idpbanca{#1}}

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
    {\bfseries\MakeUppercase{\idpautor}}\\[2\baselineskip]
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
