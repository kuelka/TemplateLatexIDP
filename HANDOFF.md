# Passagem de contexto — trabalho de implementação

Documento para quem for continuar a parte de **implementação** desta pesquisa sem ter
acompanhado o histórico. Leia inteiro antes de escrever a primeira linha.

Repositório: `https://github.com/kuelka/TemplateLatexIDP`
Estado de referência: 03/10/2026, gabarito do D1 fechado, decisões de desenho do D2 tomadas e os 51 itens do D2 conferidos;
compilação sem erros no GitHub Actions (não há LaTeX instalado na máquina do autor). Em
02/10/2026 mudaram `01-introducao.tex`, `02-referencial-teorico.tex`, `04-metodologia.tex` e
`05-resultados.tex` (ver seção 4).

---

## 1. A pesquisa em um parágrafo

Dissertação de Mestrado Profissional em Administração Pública (IDP). Propõe uma
arquitetura de IA generativa — agente único, LLM com *function calling* — que **segrega
o cálculo determinístico (Python) da geração de linguagem**, recuperando normas vigentes
por RAG, para oferecer assessoria em renda fixa (Tesouro Selic, Prefixado, IPCA+ e CDB) a
clientes de varejo de bancos públicos. A hipótese central (H1) é que essa segregação é
*necessária*, não apenas conveniente — o experimento testa isso por ablação.

---

## 2. Regras que você herda

Estão em `AGENTS.md` / `CLAUDE.md` na raiz. As que mais importam:

1. **Não escreva conteúdo acadêmico do zero.** Nada de argumentação, análise ou revisão
   de literatura por conta própria. O texto é do autor; o papel do assistente é
   estruturar, formatar, revisar, pesquisar fontes primárias e apontar inconsistências.
   Se o pedido for "escreva o capítulo sobre X", peça o material de base antes.
2. **Nunca invente referência bibliográfica.** Só entra em `referencias.bib` o que foi
   verificado em fonte real, com autor, ano, título e veículo conferidos. Faltando,
   deixe `% TODO: referencia pendente` e avise.
3. **Nunca invente número.** Todo dado numérico tem origem marcada e rastreável até
   fonte primária. Se não achar, diga que não achou.
4. **Commit e push:** desde 02/10/2026 o autor delega ao assistente os commits e pushes
   deste repositório, pela credencial já configurada na máquina dele. Nunca peça, aceite
   ou grave token ou senha. Force push e qualquer ação destrutiva continuam exigindo
   confirmação.
5. Compile após editar `.tex`/`.bib` e leia o log: `pdflatex main.tex && biber main &&
   pdflatex main.tex && pdflatex main.tex`. Zero ocorrências de `!` no log.
6. Não altere `idpthesis.cls`. Não redigite dados de `metadados.tex`.

As personas são **sintéticas**. Nenhum dado real de cliente de qualquer banco entra aqui.

---

## 3. O que já existe e está verificado

### Texto
Capítulos 1 a 4 e Anexos I a III escritos e submetidos a três varreduras de
consistência. Capítulos 5.2–5.5, 6 e 7 marcados `[PENDENTE]`, à espera da execução
empírica. 68 referências em `referencias.bib`, todas efetivamente citadas pelo menos uma
vez — mas não uma vez cada: a distribuição é desigual (por exemplo, `anbima2025`
aparece 9 vezes e `ibge2019pof` 5 vezes), então não trate isso como um a um.

### Corpus normativo (`bibliografia/normas-rag-corpus.md`)
14 documentos em três grupos, todos com texto legível por programa (decisão do autor,
02/10/2026). Dez têm PDF oficial arquivado em `bibliografia/normas/`: Res. CVM nº 30/2021;
Res. CMN nº 4.222/2013 (FGC), 4.557/2017, 4.879/2020, 4.893/2021, 4.968/2021 e 5.274/2025;
Lei nº 11.033/2004 (IR); Decreto nº 6.306/2007 (IOF); Lei nº 15.263/2025. Como 8 desses
PDFs não têm camada de texto, o texto legível das mesmas normas está em
`bibliografia/normas/texto/`, com procedência em `PROVENIENCIA.md`, junto com os 4 que
entraram em 02/10/2026: IN RFB nº 1.585/2015, Regulamento e página de Regras do Tesouro
Direto e Ato Declaratório CN nº 67/2025.

### Dataset D1 — cálculo (`dados/d1-rfl/`)
1.200 casos: 12 datas (1º dia útil de cada mês, jun/2025–mai/2026) × 4 personas ×
5 produtos × 5 prazos (15, 180, 360, 720, 1.080 dias). Gerado por `gerar-d1.py`, que
reproduz o CSV byte a byte.

Já preenchido: alíquota de IR, incidência e percentual de IOF, classificação de
suitability e conduta esperada, e as séries do BACEN (Selic meta 432, CDI 4389, IPCA
13522) para as doze datas. A Selic efetiva (1178) está em `series-bacen.csv` e é usada
só no fechamento do gabarito do Tesouro Selic.

Gabarito do RFL (`taxa_contratada_aa`, `gab_rfl_brl`, `fonte_gabarito_rfl`) preenchido
em 02/10/2026 pelo `fechar-gabarito.py`, só nos 600 casos de `calculo_rfl`. Reproduzível
byte a byte com `python3 gerar-d1.py && python3 fechar-gabarito.py`.

Estratos: 600 `calculo_rfl`, 300 `recusa_por_inadequacao`, 300 `controle_abstencao`.
**Só os 600 primeiros exercem o cálculo** — é sobre eles que a comparação do experimento
é calculada.

### Dataset D2 — normativo (`dados/d2-rag/`)
51 itens gabaritados, cada um com dispositivo e PDF de origem: 39 de recuperação
ordinária e 12 de vigência (D2b). Os 51 itens estão conferidos contra o texto vigente
(`CONFERENCIA-TEXTOS.md`): 23 em 02/10/2026, com 4 correções, e os 28 da Res. CVM nº 30/2021
e da Res. CMN nº 4.557/2017 em 03/10/2026, com 2 correções (D2-038: a 4.557 se aplica de S1
a S4; D2b-051: a versão 13 incorpora as Res. CMN nº 5.222 e 5.226/2025, e a 5.207/2025 só
produz efeitos em 1º/01/2027). Todas decididas pelo autor e aplicadas (planilha
`revisao-autor.xlsx`). Vigência conferida em 03/10/2026: CVM 30 idêntica ao consolidado da
CVM (revisão do suitability na agenda regulatória de 2026, a monitorar); 4.557 arquivada é a
versão 13 do BCB, a mais recente.

### Implementação de referência (`dados/d1-rfl/rfl_referencia.py`)
Calcula o RFL a partir de tabelas tributárias verificadas, com contagem de dias úteis a
partir de feriados calculados (Páscoa por Meeus). 42 verificações no autoteste
(`python3 rfl_referencia.py`).

---

## 4. Decisões já tomadas

**Rota A para o descasamento de vencimento (23/09/2026).** Os prazos de 15, 180, 360,
720 e 1.080 dias ficam como estão, e a taxa do título de vencimento mais próximo é usada
como aproximação, sob premissa declarada de curva plana. Consequência a registrar na
metodologia: o RFL do Prefixado deixa de ser exato, porque o resgate ocorre antes do
vencimento — ou, em 135 dos 360 casos de Tesouro, depois dele, com reinvestimento
implícito à mesma taxa (limitação declarada; ver seção 5 e o README do D1).

**Granularidade mensal** do D1, com 1.200 registros, incluindo o CDB acima do teto do FGC.

**Desenho do D2 e da base RAG (02/10/2026).**
- Nenhum item excluído: a metodologia passou de "30 a 50 perguntas" para 39 perguntas mais
  um subconjunto adicional de 12 de vigência.
- Métricas: recall@k com k = 1, 3, 5 e 10 e MRR no lugar da precisão; no D2b, proporção de
  perguntas com a redação vigente recuperada antes da revogada. k operacional provisório: 5.
- Corpus de 14 documentos, pelo critério de que toda regra aplicada pelo agente precisa da
  norma que a sustenta. Precedência: norma > Regulamento do TD > página de Regras do TD.
- A ANBIMA saiu das descrições da base RAG (objetivo d, figura e referencial), porque não
  tem documento no corpus; continua como fonte de dados.

---

## 5. Premissas — estado em 02/10/2026

**Fixadas (não são escolha; são convenção de mercado ou lei):**

- Capitalização em base 252 dias úteis; IR e IOF em dias corridos.
- Base do IR = rendimento bruto líquido do IOF (IN RFB nº 1.585/2015, art. 46, § 1º).
  A custódia da B3 **não** reduz a base: sai do valor recebido. 0,20% a.a. sobre o valor
  **atualizado** da posição, provisionada dia a dia (não sobre o valor aplicado); Tesouro
  Selic isento até R$ 10.000 por CPF.

**Decididas pelo autor:**

- CDB a 94,0% do CDI: mediana dos oito últimos meses oficiais do BCB (jun/2023–jan/2024),
  porque as séries de taxa de CDB estão suspensas desde jan/2024. Extrapolação declarada.

- Produto inadequado: o sistema **não recomenda nem informa rentabilidade**. Os 300 casos de
  recusa ficam sem RFL.
- Prazo × vencimento do Tesouro: Rota A (seção 4), **mantida** em 02/10/2026 mesmo
  sabendo que em 135 dos 360 casos de Tesouro o título vence antes do resgate (limitação
  declarada no README do D1). Não troque a regra de seleção sem decisão do autor.
- Datas efetivas (02/10/2026): no Tesouro, o prazo conta entre as **liquidações** (aplicação
  em D+1 útil), regra do Tesouro Nacional de 2018 para o IRRF; no CDB, da data de
  aplicação. Resgate que cairia em dia sem expediente é **antecipado para o dia útil
  anterior**, para nenhum caso mudar de faixa de IR. IR e IOF usam `dias_corridos`. Regra
  em `rfl_referencia.datas_efetivas()`; colunas `data_inicio`, `data_resgate` e
  `dias_corridos` no `d1-casos.csv`.

**Em aberto — não decida pelo autor:**

1. **CDB × carência para Marina e Antônio** (72 casos): restringir a célula por prazo,
   redefinir o produto como CDB com cláusula de resgate antecipado (termo do BCB, que não
   equivale a liquidez diária), ou abrir a matriz por prazo.

---

## 6. Próximas tarefas, em ordem

**(a) Extrair as taxas do Tesouro. FEITO em 23/09/2026.** O autor baixou o
`precotaxatesourodireto.csv` e rodou `dados/d1-rfl/extrair-tesouro.py` sobre o arquivo
real (176.390 linhas; tamanho e SHA-256 em `tesouro-PROVENIENCIA.txt`). Ver
`dados/d1-rfl/COMO-EXTRAIR-TESOURO.md`.

**(b) Fechar o gabarito do D1. FEITO em 02/10/2026**, inclusive a conferência amostral. Gabarito
pelo `fechar-gabarito.py`. Tesouro conferido contra a calculadora avançada do Tesouro
Direto (132 casos; `dados/d1-rfl/conferencia-tesouro/CONFERENCIA.md`); mecânica do CDB
conferida contra a Calculadora do Cidadão do BCB com CDI realizado (28 períodos;
`dados/d1-rfl/conferencia-cdb/CONFERENCIA.md`). Resultado citado em `fonte_gabarito_rfl`.

**(c) Escrever o módulo Python do RFL** — objetivo específico (c), o que o agente chama
por *function calling*. *Critério de aceite*: reproduz o gabarito dentro do limiar de
tolerância. **Não pode importar `rfl_referencia.py`, nem o contrário.**

**(d) Construir a base RAG** — objetivo (d), sobre o corpus de 14 documentos (`bibliografia/normas-rag-corpus.md`), com metadados
de vigência. *Critério de aceite*: recall@k (k = 1, 3, 5 e 10) e MRR medidos no D2, e, no D2b, a
proporção de perguntas com a redação vigente recuperada antes da revogada (decisão do
autor, 02/10/2026). k operacional provisório: 5, a confirmar pela curva de recall.

**(e) Montar o agente e rodar o experimento de ablação**: arquitetura completa versus o
mesmo LLM sem acesso ao módulo Python, mesma bateria de perguntas.

---

## 7. Armadilhas já encontradas — não repita

**Circularidade do gabarito.** O gabarito do D1 **não pode** sair do módulo que o
experimento avalia. São duas implementações independentes que se conferem, ambas
ancoradas em simulador oficial.

**Ágio × deságio no Tesouro Selic.** Na LFT, taxa de compra positiva significa PU abaixo
do valor nominal atualizado — **deságio**. Negativa é ágio. O rótulo estava invertido e
foi corrigido em 02/10/2026; os números não mudaram.

**Custódia sobre o valor aplicado.** A B3 calcula a taxa sobre o valor atualizado da
posição, provisionada dia a dia. A primeira versão cobrava sobre o valor aplicado e
subestimava a custódia em até R$ 2,44 por caso (corrigido em 02/10/2026).

**Fronteira do IR no dia 360.** A faixa de 20% vai até o 360º dia inclusive; 361 já é
17,5%. Um caso de 365 dias paga 17,5%, não 20% — esse erro passou e foi pego pelo
autoteste.

**Marina e Antônio têm capacidade idêntica** (R$ 335,18/mês, mesma classe de rendimento
da POF). Não é erro de digitação.

**João tem capacidade nula** por superávit financeiro negativo da classe. Os 300 casos
dele testam **abstenção**, não cálculo — e a abstenção é achado ancorado no art. 6º, I da
Res. CVM nº 30/2021, não limitação do estudo.

**Os casos de CDB acima do FGC** usam estoque hipotético de R$ 300.000, porque nenhuma
persona chega a R$ 250.000 pelo aporte mensal. Está marcado em `origem_valor`.

**Prazos longos terminam no futuro.** 1.080 dias a partir de 2026 vencem em 2029. O RFL
do D1 é projeção sob premissa declarada, como faz um simulador — não retorno realizado.
Isso o distingue do backtesting de doze meses do Capítulo 4.

**A H2 não tem desenho de teste** em lugar nenhum — nem no Capítulo 4, nem no Anexo III.
Decisão pendente do autor: rebaixá-la a implicação discutida ou criar um objetivo
específico (f).

**Rede.** No ambiente onde este pacote foi montado, a API do BACEN só respondeu por
ferramenta de fetch, e o Tesouro Transparente não respondeu de jeito nenhum. Se seu
ambiente bloquear, não contorne inventando número: peça o arquivo ao autor.

**Push bloqueado pelo proxy da sessão.** Em ambiente com proxy de rede, o push só passa
se o repositório estiver entre as fontes autorizadas da sessão. Se o proxy recusar
("not in this session's authorized repository set"), **não desligue o proxy nem tente
contorná-lo**: peça ao autor que adicione o repositório às fontes da sessão, ou gere um
patch (`git format-patch`) para ele aplicar e enviar da máquina dele.

---

## 8. Pendências menores

- Legenda da matriz do Anexo III ainda marcada "(a confirmar com o orientador)".
- `apendices/apendice-a.tex` continua com o texto-modelo do template.
- ~~D2 tem 51 itens; o documento de alinhamento fala em "30 a 50".~~ Resolvido em 02/10/2026: metodologia
  ajustada para 39 + 12 e sem a ANBIMA no conjunto de teste.
- ~~Revisão do autor nos 28 itens do D2 fora da conferência.~~ Feita em 03/10/2026 (2 correções).
- Monitorar até a defesa a revisão da Res. CVM nº 30/2021 (agenda regulatória de 2026 da CVM) e
  a entrada em vigor da Res. CMN nº 5.207/2025 em 1º/01/2027.
- URL de origem e data do download de `bibliografia/dados/bcb-depositos-prazo-ValoresNatDetentores.xls`,
  marcadas como pendentes em `bibliografia/README.md` — a informar pelo autor.
- Convenção de dias da provisão da custódia (adotada: dias úteis, base 252, porque o
  regulamento não especifica) — o autor pode preferir dias corridos.
