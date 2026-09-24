# Passagem de contexto — trabalho de implementação

Documento para quem for continuar a parte de **implementação** desta pesquisa sem ter
acompanhado o histórico. Leia inteiro antes de escrever a primeira linha.

Repositório: `https://github.com/kuelka/TemplateLatexIDP`
Estado de referência: commit `1a402fd`, 23/09/2026, 53 páginas, compilação sem erros.

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
4. **Commit e push só quando o autor pedir.** Nunca autentique no GitHub. Se ele
   oferecer token ou senha, recuse e oriente a revogar.
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

### Corpus normativo (`bibliografia/normas/`)
Dez PDFs oficiais arquivados e conferidos contra texto oficial: Res. CVM nº 30/2021
(suitability, texto consolidado); Res. CMN nº 4.222/2013 (FGC); 4.557/2017; 4.879/2020;
4.893/2021; 4.968/2021; 5.274/2025; Lei nº 11.033/2004 (IR); Decreto nº 6.306/2007
(IOF); Lei nº 15.263/2025 (linguagem simples).

### Dataset D1 — cálculo (`dados/d1-rfl/`)
1.200 casos: 12 datas (1º dia útil de cada mês, jun/2025–mai/2026) × 4 personas ×
5 produtos × 5 prazos (15, 180, 360, 720, 1.080 dias). Gerado por `gerar-d1.py`, que
reproduz o CSV byte a byte.

Já preenchido: alíquota de IR, incidência e percentual de IOF, classificação de
suitability e conduta esperada, e as séries do BACEN (Selic meta 432, CDI 4389, IPCA
13522) para as doze datas.

Ainda vazio: `taxa_contratada_aa`, `gab_rfl_brl`, `fonte_gabarito_rfl`.

Estratos: 600 `calculo_rfl`, 300 `recusa_por_inadequacao`, 300 `controle_abstencao`.
**Só os 600 primeiros exercem o cálculo** — é sobre eles que a comparação do experimento
é calculada.

### Dataset D2 — normativo (`dados/d2-rag/`)
51 itens gabaritados, cada um com dispositivo e PDF de origem: 39 de recuperação
ordinária e 12 de vigência (D2b). Pendente de revisão item a item pelo autor.

### Implementação de referência (`dados/d1-rfl/rfl_referencia.py`)
Calcula o RFL a partir de tabelas tributárias verificadas, com contagem de dias úteis a
partir de feriados calculados (Páscoa por Meeus). 28 verificações no autoteste.

---

## 4. Decisões já tomadas

**Rota A para o descasamento de vencimento (23/09/2026).** Os prazos de 15, 180, 360,
720 e 1.080 dias ficam como estão, e a taxa do título de vencimento mais próximo é usada
como aproximação, sob premissa declarada de curva plana. Consequência a registrar na
metodologia: o RFL do Prefixado deixa de ser exato, porque o resgate ocorre antes do
vencimento.

**Granularidade mensal** do D1, com 1.200 registros, incluindo o CDB acima do teto do FGC.

---

## 5. Premissas que o AUTOR ainda precisa declarar

Não as escolha por ele. Elas estão como parâmetros obrigatórios em `rfl_referencia.py`.

1. **Convenção de capitalização**: `"252"` (dias úteis, padrão do mercado) ou `"365"`.
   É a de maior consequência — se divergir entre o módulo do objetivo (c) e a
   implementação de referência, a taxa de erro medida vira artefato da divergência, não
   evidência sobre a H1.
2. **Percentual do CDI** adotado para o CDB. Não é dado público.
3. **Taxa de custódia da B3** e sua ordem de incidência. Hoje o módulo deduz do montante
   bruto antes de apurar a base tributável. O Tesouro Selic é isento até certo valor.
4. **Conduta esperada quando o cliente pergunta a rentabilidade de produto inadequado**:
   calcular e sinalizar, ou recusar? Define o gabarito de 300 dos 1.200 registros.

---

## 6. Próximas tarefas, em ordem

**(a) Extrair as taxas do Tesouro.** O autor baixa o `precotaxatesourodireto.csv` e roda
`dados/d1-rfl/extrair-tesouro.py`. Ver `dados/d1-rfl/COMO-EXTRAIR-TESOURO.md`. O script
foi testado só contra arquivo sintético — confira o cabeçalho impresso na primeira
execução.

**(b) Fechar o gabarito do D1.** Rodar `rfl_referencia.py` sobre os 600 casos de cálculo,
preenchendo as três colunas vazias. *Critério de aceite*: uma amostra conferida contra
simulador oficial (Tesouro Direto, calculadora ANBIMA), com o resultado da conferência
registrado em `fonte_gabarito_rfl`.

**(c) Escrever o módulo Python do RFL** — objetivo específico (c), o que o agente chama
por *function calling*. *Critério de aceite*: reproduz o gabarito dentro do limiar de
tolerância. **Não pode importar `rfl_referencia.py`, nem o contrário.**

**(d) Construir a base RAG** — objetivo (d), sobre o corpus de dez normas, com metadados
de vigência. *Critério de aceite*: recall@k e precisão medidos no D2, com o D2b
demonstrando priorização da redação vigente.

**(e) Montar o agente e rodar o experimento de ablação**: arquitetura completa versus o
mesmo LLM sem acesso ao módulo Python, mesma bateria de perguntas.

---

## 7. Armadilhas já encontradas — não repita

**Circularidade do gabarito.** O gabarito do D1 **não pode** sair do módulo que o
experimento avalia. São duas implementações independentes que se conferem, ambas
ancoradas em simulador oficial.

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

---

## 8. Pendências menores

- Legenda da matriz do Anexo III ainda marcada "(a confirmar com o orientador)".
- `apendices/apendice-a.tex` continua com o texto-modelo do template.
- D2 tem 51 itens; o documento de alinhamento fala em "30 a 50".
- Revisão item a item do D2 pelo autor, antes de qualquer uso.
