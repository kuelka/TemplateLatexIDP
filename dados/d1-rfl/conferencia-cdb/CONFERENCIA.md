# Conferência do CDB do D1 contra a Calculadora do Cidadão (BCB)

**Data:** 02/10/2026 · **Resultado:** a mecânica de capitalização do CDB em
`rfl_referencia.py` reproduz os 28 índices da calculadora do BCB até a 8ª casa decimal
(diferença máxima de 5 × 10⁻⁹).

## O que se confere

A Calculadora do Cidadão (Correção de valores > CDI) corrige um valor pelo **CDI
realizado** entre duas datas, a um percentual do CDI. O gabarito do D1 **projeta** o CDI
constante a partir da aplicação, como faz um simulador. Os números do gabarito, portanto,
não são comparáveis diretamente com os da calculadora.

O que se confere é a mecânica, aplicando a regra do gabarito ao CDI realizado:

- 94% do CDI aplicado sobre a taxa **diária** do CDI;
- capitalização composta por dia útil;
- calendário de dias úteis de `rfl_referencia.py`;
- convenção do intervalo [data inicial, data final): conta-se o dia da aplicação e não o
  do resgate.

Os tributos (IR e IOF) não entram aqui, porque a calculadora corrige só o valor bruto. A
alíquota e a base do IR foram conferidas contra a calculadora do Tesouro
(`../conferencia-tesouro/CONFERENCIA.md`).

## Fontes

| Item | Origem |
|---|---|
| Calculadora | BCB, Calculadora do Cidadão, `https://www3.bcb.gov.br/CALCIDADAO/publico/exibirFormCorrecaoValores.do?method=exibirFormCorrecaoValores` (aba CDI), consultada em 02/10/2026 com valor de R$ 1.000,00 e 94,00% do CDI. Respostas em `calculadora-cidadao.json`: aplicação, resgate do D1, datas usadas pela calculadora e índice de correção |
| CDI diário | BCB/SGS, série 12, JSON bruto de `https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=json&dataInicial=01/06/2025&dataFinal=02/10/2026`, 338 observações de 02/06/2025 a 01/10/2026, guardadas por trechos em `cdi-sgs12.json`. As taxas diárias reproduzem o CDI anual de `series-bacen.csv` (por exemplo, 0,054266% a.d. corresponde a 14,65% a.a.). As 338 datas coincidem em número com os dias úteis do calendário da referência, e 20/11/2025 não consta da série |

## Amostra

Os 28 pares de datas (`data_aplicacao`, `data_resgate`) dos 112 casos de CDB do estrato
`calculo_rfl` cujo resgate já ocorreu até 01/10/2026: todos os prazos de 15 dias, 44 dos 48 de 180 dias
e 20 dos 48 de 360 dias. O índice independe do valor aplicado, por isso basta um cálculo
por par. Os prazos de 720 e 1.080 dias ainda não terminaram.

## Datas de resgate

As datas são as colunas `data_aplicacao` e `data_resgate` do `d1-casos.csv`. Pela regra
adotada em 02/10/2026 (`rfl_referencia.datas_efetivas()`), o resgate que cairia em dia sem
expediente é antecipado para o dia útil anterior, e o CDB conta o prazo a partir da data de
aplicação. Na primeira rodada, feita antes dessa regra, a calculadora avisou que, quando a
data final não é dia útil, usa o dia útil seguinte. Na rodada atual todas as datas finais já
são dias úteis, e a calculadora usou as datas informadas em todos os 28 períodos.

## Reprodução

```bash
cd dados/d1-rfl/conferencia-cdb && python3 comparar.py
```
