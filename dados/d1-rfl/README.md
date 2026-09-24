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
| `taxa_contratada_aa` | **vazia — pendente** |
| `gab_rfl_brl` | **vazia — pendente** |
| `fonte_gabarito_rfl` | **vazia — pendente** |

## O que falta para fechar o gabarito

Das séries de mercado, as do BACEN já estão coletadas e arquivadas (`series-bacen.csv`).
Restam quatro itens, três deles decisões do autor:

1. **Taxas do Tesouro Prefixado e IPCA+** nas doze datas. O BACEN não publica taxas
   contratadas do Tesouro Direto. A fonte é o Tesouro Transparente, arquivo
   `precotaxatesourodireto.csv`; o recurso não tem datastore ativo, então não há consulta
   filtrada — o arquivo completo precisa ser baixado e arquivado no repositório.
2. **Ágio ou deságio do Tesouro Selic** sobre a meta. A LFT é negociada a "Selic + x%",
   e esse `x` também vem do Tesouro Transparente. A meta isolada não fecha a taxa.
3. **Percentual do CDI adotado para o CDB.** Não é dado público — é premissa
   institucional, que precisa ser declarada explicitamente na metodologia.
4. **Convenção de capitalização.** Os prazos do dataset estão em dias corridos, porque é
   assim que IR e IOF incidem, mas a remuneração de renda fixa no Brasil capitaliza em
   dias úteis (base 252). A conversão exige calendário de feriados até 2029, já que os
   prazos de 1.080 dias a partir de 2026 terminam naquele ano. A regra de conversão é
   decisão metodológica e precisa ser fixada antes de qualquer cálculo.

Fixados esses quatro pontos, falta ainda a **implementação de referência** do cálculo do
RFL, **independente do módulo Python sob teste**, conferida por amostragem contra
simuladores oficiais. O gabarito não pode ser produzido pelo próprio módulo que o
experimento avalia — seria circular.

## Decisão sobre o horizonte (23/09/2026) — Rota A

O Tesouro não oferta títulos com prazo arbitrário, e quase nunca há vencimento
coincidente com os horizontes de 15, 180, 360, 720 e 1.080 dias. Optou-se por **manter
os prazos** e usar a taxa do vencimento mais próximo como aproximação, sob premissa
declarada de curva plana. Consequência a registrar na metodologia: o RFL do Prefixado
deixa de ser exato e passa a depender dessa premissa, porque o resgate ocorre antes do
vencimento. Ver `COMO-EXTRAIR-TESOURO.md`, seção 3.

## Nota sobre o horizonte dos prazos

Os prazos de 720 e 1.080 dias, a partir das datas finais da janela, terminam em 2028 e
2029. O RFL desses casos não é, portanto, retorno **realizado**, e sim projeção sob
premissa declarada na data de aplicação — que é o que um simulador oficial faz. Para o
Prefixado a taxa é contratada e a projeção é exata; para Tesouro Selic, CDB e IPCA+ ela
depende de premissa sobre a trajetória futura do indexador. Isso distingue o dataset D1
do backtesting de doze meses descrito no Capítulo 4, que mede retorno realizado.

## Decisões que ficaram registradas aqui e ainda cabem ao orientador

1. **Valor dos casos de CDB acima do FGC.** Nenhuma persona alcança R$ 250.000 pelo fluxo
   mensal de aporte, de modo que esses casos usam um estoque hipotético de R$ 300.000
   (acima do teto por conglomerado, abaixo do teto global de R$ 1.000.000 por CPF em
   quatro anos). É a mesma premissa sob a qual a célula foi classificada na matriz do
   Anexo III. Está marcado em `origem_valor`.
2. **Perguntas de cálculo sobre produto inadequado.** Os 300 registros do estrato
   `recusa_por_inadequacao` hoje não têm RFL esperado. Um cliente pode perguntar a
   rentabilidade de um produto que lhe é inadequado, e há duas condutas defensáveis —
   calcular e sinalizar a inadequação, ou recusar. A escolha altera o gabarito desses
   registros.
3. **Redundância do estrato de abstenção.** Os 300 registros da persona sem capacidade
   têm resposta invariante quanto a produto e prazo; variam só na data. Sustentam que a
   abstenção se mantém sob qualquer condição de mercado, mas podem ser reduzidos se o
   orientador preferir um desenho mais enxuto.
4. **Limiar de tolerância** do desvio percentual entre RFL reportado e RFL calculado
   — segue sem valor fixado no texto.

## Calendário

Os feriados bancários usados no cálculo do 1º dia útil estão listados no gerador e
devem ser conferidos contra o calendário ANBIMA antes do uso definitivo.
