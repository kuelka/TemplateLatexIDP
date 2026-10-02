# Dataset D1 — Perguntas de cálculo de Retorno Final Líquido

**Gerado em:** 23/09/2026 · **Gerador:** `gerar-d1.py` · **Saída:** `d1-casos.csv` (1.200 registros)

Conjunto de casos de teste que operacionaliza o experimento de *ablation* descrito no
Capítulo 4 (Técnicas de Análise dos Dados) e no documento de alinhamento de 21/08/2026.
Granularidade mensal, definida pelo autor em 23/09/2026.

## Dimensões

| Dimensão | Valores | n |
|---|---|---|
| Data de aplicação | 1º dia útil de cada mês, jun/2025–mai/2026 | 12 |
| Persona | P1 João, P2 Marina, P3 Antônio, P4 Rafael (Anexo II) | 4 |
| Produto | Tesouro Selic, Prefixado, IPCA+, CDB dentro e acima do FGC | 5 |
| Prazo | 15, 180, 360, 720, 1.080 dias | 5 |

12 × 4 × 5 × 5 = **1.200**

Os cinco prazos cruzam todas as fronteiras tributárias: 15 dias é o único caso com
incidência de IOF (50% do rendimento), e os demais isolam cada uma das quatro faixas
da tabela regressiva de IR (22,5% / 20% / 17,5% / 15%).

## Estratos

| Estrato | n | O que testa |
|---|---|---|
| `calculo_rfl` | 600 | Fidelidade do RFL reportado — é sobre este estrato que a comparação entre a arquitetura completa e a condição de controle é calculada |
| `recusa_por_inadequacao` | 300 | Células `I` da matriz: recusa de produto inadequado (art. 6º, I, Res. CVM nº 30/2021) |
| `controle_abstencao` | 300 | Persona sem capacidade de investimento: abstenção de recomendar qualquer produto |

## Esquema

| Coluna | Origem |
|---|---|
| `id`, `data_aplicacao`, `persona_*`, `produto_*`, `prazo_dias` | enumeração |
| `valor_aplicado_brl`, `origem_valor` | capacidade mensal do Anexo II (POF/IBGE) ou estoque hipotético |
| `estrato`, `gab_tipo` | derivados |
| `gab_aliquota_ir` | **Lei nº 11.033/2004, art. 1º** — conferida em texto oficial |
| `gab_iof_incide`, `gab_iof_pct_rendimento` | **Decreto nº 6.306/2007, art. 32 e Anexo** — conferido caractere a caractere no PDF oficial |
| `gab_suitability`, `gab_conduta_esperada` | **Anexo III, seção III.2** (matriz 4×5) |
| `selic_meta_aa`, `cdi_aa`, `ipca_12m_aa`, `ipca_mes_referencia` | **BACEN/SGS, séries 432, 4389 e 13522** — coletadas em 23/09/2026, ver `series-bacen-PROVENIENCIA.md` |
| `taxa_contratada_aa` | `fechar-gabarito.py` — preenchida só no estrato `calculo_rfl` (600 casos) |
| `gab_rfl_brl` | `fechar-gabarito.py`, via `rfl_referencia.py` — só no estrato `calculo_rfl` |
| `fonte_gabarito_rfl` | `fechar-gabarito.py` — origem da taxa e estado da conferência contra simulador oficial |

## O que falta para fechar o gabarito

Resolvidos em 23/09 e 02/10/2026:

- **Taxas do Tesouro Prefixado e IPCA+ e taxa de compra do Tesouro Selic** (positiva =
  deságio, negativa = ágio) — extraídas do Tesouro
  Transparente pelo `extrair-tesouro.py` (176.390 linhas lidas, 200 no recorte, SHA-256
  do original registrado em `tesouro-PROVENIENCIA.txt`).
- **Convenção de capitalização** — não é escolha: base 252 dias úteis para remuneração e
  dias corridos para IR e IOF, convenção consolidada do mercado.
- **Base do IR e custódia** — não é escolha: a base é o rendimento bruto líquido do IOF
  (IN RFB nº 1.585/2015, art. 46, § 1º; MAFON, código 8053). A custódia da B3 (0,20% a.a.,
  Tesouro Selic isento até R$ 10.000 por CPF) é deduzida do valor recebido, **fora** da
  base do imposto.
- **Base da custódia** — não é escolha: o Regulamento do Tesouro Direto manda calculá-la
  "sobre o valor dos títulos" e provisioná-la diariamente, ou seja, sobre o valor
  atualizado da posição, não sobre o valor aplicado (corrigido em 02/10/2026; alterou o
  RFL de 145 casos de Prefixado e IPCA+, no máximo R$ 2,44). O regulamento não fixa a
  contagem de dias da provisão; adotou-se a da remuneração (dias úteis, base 252).

**Gabarito do RFL fechado em 02/10/2026** pelo `fechar-gabarito.py`, para os 600 casos
do estrato `calculo_rfl`. Para reproduzir: `python3 gerar-d1.py && python3 fechar-gabarito.py`.

Premissas declaradas no cabeçalho do script:

- **CDB a 94,0% do CDI.** As séries de taxa de CDB do BCB (28663 mensal; 40 diária PF)
  estão suspensas desde 31/01/2024, e as Estatísticas de depósitos a prazo do BCB
  (semestrais) publicam só estoques, sem taxa. Adotou-se a mediana dos oito últimos meses
  oficiais (jun/2023–jan/2024; média 94,4%, faixa 91,5%–97,1%) — extrapolação declarada.
- **Indexadores constantes** a partir da data de aplicação: Selic efetiva (SGS 1178),
  CDI (SGS 4389) e IPCA em 12 meses (SGS 13522, última leitura publicada).
- **Tesouro pela Rota A**, com a taxa de compra do vencimento mais próximo e curva plana.

Conferência: um caso recalculado de forma independente do módulo (Rafael, CDB, 02/06/2025,
360 dias) bateu no centavo (RFL R$ 211,68).

Em aberto:

- **Conferência amostral contra simulador oficial** (Tesouro Direto, calculadora ANBIMA),
  registrada como PENDENTE em `fonte_gabarito_rfl`.
- **CDB × carência para Marina e Antônio** (72 casos hoje classificados como A). As
  Estatísticas de depósitos a prazo do BCB mostram que 65,3% (jun/2025) e 67,9% (dez/2025)
  do estoque detido por pessoas físicas e jurídicas tem cláusula de resgate antecipado.

## Decisão sobre o horizonte (23/09/2026) — Rota A

O Tesouro não oferta títulos com prazo arbitrário, e quase nunca há vencimento
coincidente com os horizontes de 15, 180, 360, 720 e 1.080 dias. Optou-se por **manter
os prazos** e usar a taxa do vencimento mais próximo como aproximação, sob premissa
declarada de curva plana. Consequência a registrar na metodologia: o RFL do Prefixado
deixa de ser exato e passa a depender dessa premissa, porque o resgate ocorre antes do
vencimento. Ver `COMO-EXTRAIR-TESOURO.md`, seção 3.

**Limitação declarada (02/10/2026): título que vence antes do resgate.** A regra do
vencimento mais próximo escolhe, em **135 dos 360 casos de Tesouro** do estrato
`calculo_rfl` (37,5%; 69 de Tesouro Selic, 46 de Prefixado e 20 de IPCA+), um título que
vence **antes** da data de resgate — `gap_dias` negativo em `tesouro-selecao.csv`, até
495 dias. Nesses casos não há venda antecipada nem marcação a mercado: a curva plana
equivale a supor que o valor recebido no vencimento é reinvestido à mesma taxa até o
resgate, e o gabarito aplica a alíquota de IR do prazo do D1, não a do prazo efetivo até
o vencimento (que pode cair em faixa diferente). O autor manteve a regra por decisão de
método em 02/10/2026; a alternativa avaliada — vencimento mais próximo igual ou
posterior ao resgate — eliminaria o reinvestimento, mas alteraria 66 das 180 seleções e
elevaria o descasamento mediano de 121 para 209 dias (máximo de 495 para 992).

## Nota sobre o horizonte dos prazos

Os prazos de 720 e 1.080 dias, a partir das datas finais da janela, terminam em 2028 e
2029. O RFL desses casos não é, portanto, retorno **realizado**, e sim projeção sob
premissa declarada na data de aplicação — que é o que um simulador oficial faz. Para o
Prefixado a taxa é contratada, mas pela Rota A a projeção depende da premissa de curva
plana (seção anterior); para Tesouro Selic, CDB e IPCA+ ela depende também de premissa
sobre a trajetória futura do indexador. Isso distingue o dataset D1
do backtesting de doze meses descrito no Capítulo 4, que mede retorno realizado.

## Decisões que ficaram registradas aqui e ainda cabem ao orientador

1. **Valor dos casos de CDB acima do FGC.** Nenhuma persona alcança R$ 250.000 pelo fluxo
   mensal de aporte, de modo que esses casos usam um estoque hipotético de R$ 300.000
   (acima do teto por conglomerado, abaixo do teto global de R$ 1.000.000 por CPF em
   quatro anos). É a mesma premissa sob a qual a célula foi classificada na matriz do
   Anexo III. Está marcado em `origem_valor`.
2. **Perguntas de cálculo sobre produto inadequado — decidido em 02/10/2026.** O sistema
   não recomenda **nem informa a rentabilidade** de produto inadequado. Os 300 registros do
   estrato `recusa_por_inadequacao` permanecem sem RFL esperado e testam a recusa. A opção
   de calcular e sinalizar foi descartada por aumentar o volume de verificação em 300 casos.

3. **Redundância do estrato de abstenção.** Os 300 registros da persona sem capacidade
   têm resposta invariante quanto a produto e prazo; variam só na data. Sustentam que a
   abstenção se mantém sob qualquer condição de mercado, mas podem ser reduzidos se o
   orientador preferir um desenho mais enxuto.
4. **Limiar de tolerância** do desvio percentual entre RFL reportado e RFL calculado
   — segue sem valor fixado no texto.

## Calendário

Os feriados bancários usados no cálculo do 1º dia útil estão listados no gerador e
devem ser conferidos contra o calendário ANBIMA antes do uso definitivo.
