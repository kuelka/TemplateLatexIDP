# Conferência do gabarito do D1 contra a calculadora oficial do Tesouro Direto

**Data:** 02/10/2026 · **Escopo:** casos de Tesouro do estrato `calculo_rfl` · **Resultado:**
132 de 360 casos conferidos. O prazo do IR bate em 132 de 132, e o valor bruto bate até
R$ 0,03 quando se usam os mesmos dias úteis. Nenhuma diferença aponta erro de cálculo em
`rfl_referencia.py`; as que restam têm origem identificada na própria calculadora.

Esta é a segunda rodada. A primeira, também de 02/10/2026, usava o prazo contado a partir da
data de aplicação e levou o autor a adotar a regra do Tesouro Nacional de 2018: no Tesouro,
o prazo conta entre as liquidações, e o resgate que cairia em dia sem expediente é
antecipado para o dia útil anterior (`rfl_referencia.datas_efetivas()`). As colunas
`data_inicio`, `data_resgate` e `dias_corridos` do `d1-casos.csv` registram essas datas.

## 1. Fontes

| Item | Origem |
|---|---|
| Calculadora | Tesouro Direto, Calculadora avançada (`https://www.tesourodireto.com.br/simuladores/calculadora-avancada`). O próprio formulário chama `POST /o/calculadora-avancada`, e as consultas foram feitas nesse endereço. Respostas registradas entre 19:45:49 e 19:47:03 de 02/10/2026 (campo `BizSts.dtTm`). Uma consulta (D1-0483) falhou na primeira tentativa com erro 400 do servidor e foi repetida |
| Ressalva da fonte | A página avisa que os resultados são "apenas exemplificativos". A calculadora serve aqui como conferência independente da aritmética, não como valor oficial de liquidação |
| Regras do Tesouro Direto | Página "Regras e Regulamento" (`https://www.tesourodireto.com.br/sobre-o-tesouro/regras-e-regulamento`), consultada em 02/10/2026: custódia de 0,2% a.a. sobre o valor dos títulos, provisionada diariamente a partir da liquidação da compra (D+1); Tesouro Selic isento até R$ 10.000,00 por CPF; prazo do IRRF contado entre as datas de **liquidação** da aplicação e do resgate (orientação do Tesouro Nacional de 2018); resgate pedido em dia útil entre 9h30 e 13h liquida no mesmo dia |
| Calendário | ANBIMA, `https://www.anbima.com.br/feriados/arqs/feriados_nacionais.xls`, baixado em 02/10/2026, 111.104 bytes, SHA-256 `e3070152bfbdd733a27977adc82b799e973d3ea003d2aa25b0e7e5bdae63aa17`. De 2025 a 2029, os feriados batem um a um com `feriados_nacionais()` de `rfl_referencia.py` |

## 2. Amostra

Entraram **todos** os casos de Tesouro do estrato `calculo_rfl` que a calculadora aceita.
São três restrições da própria calculadora:

1. o título ainda precisa estar listado (os vencimentos de 2026 já saíram);
2. a data de resgate não pode passar do vencimento;
3. a taxa de compra precisa ser positiva (deságio). Taxa zero ou ágio é recusada.

Em cada consulta: data de compra = `data_aplicacao`; data de resgate = `data_resgate`; taxa
de venda igual à de compra (a premissa de curva plana da Rota A); taxa da instituição
financeira zero.

| Produto | 15 | 180 | 360 | 720 | 1.080 |
|---|---|---|---|---|---|
| Tesouro Selic | 3/36 | 3/36 | 18/36 | 18/36 | 18/36 |
| Tesouro Prefixado | 10/24 | 10/24 | 12/24 | 12/24 | 12/24 |
| Tesouro IPCA+ | 0/12 | 0/12 | 0/12 | 4/12 | 12/12 |

As datas de aplicação vão de 02/06/2025 a 04/05/2026. Ficam sem cobertura o IPCA+ de 15,
180 e 360 dias (todos usam a NTN-B Principal de 15/08/2026, já vencida) e os 135 casos em
que o título vence antes do resgate. O CDB foi conferido à parte, contra a Calculadora do
Cidadão do BCB (`../conferencia-cdb/CONFERENCIA.md`).

## 3. O que bate

- **Prazo do IR (dias corridos entre as liquidações):** igual em 132 de 132. A calculadora
  conta da liquidação da compra (D+1 útil) até a data do resgate, como a referência.
- **Alíquota de IR:** igual em 132 de 132.
- **Aritmética da remuneração:** com os mesmos dias úteis da calculadora, o montante bruto
  da referência difere no máximo R$ 0,03 (132 de 132).
- **Base do IR:** a calculadora cobra IR sobre bruto menos aplicado, sem descontar a
  custódia (IN RFB nº 1.585/2015, art. 46, § 1º).
- **Valor líquido:** bruto menos IR menos custódia, a mesma ordem da referência.
- **Custódia sobre o valor atualizado:** no Prefixado e no IPCA+, a diferença é de centavos
  (máximo R$ 0,29).

## 4. Diferenças e sua origem

| # | Diferença | Casos | Efeito máximo no RFL | Origem | Tratamento |
|---|---|---|---|---|---|
| 1 | A calculadora remunera também o dia do resgate: conta dias úteis de D+1 da compra até D+1 do resgate | 132 | 1 dia útil | A referência supõe resgate pedido entre 9h30 e 13h, que liquida no mesmo dia; a calculadora age como se a venda liquidasse em D+1 | Premissa declarada da referência; mantida |
| 2 | A calculadora trata 20/11 como dia útil | os casos com 20/11/2025 ou 20/11/2026 no prazo | 1 dia útil por ocorrência | 20/11 é feriado nacional desde 2024 (Lei nº 14.759/2023), consta do calendário ANBIMA e não tem CDI na série 12 do BCB | Defeito da calculadora; referência mantida |
| 3 | A calculadora não cobra IOF | 13 de 15 dias | R$ 5,95 | IOF regressivo do Decreto nº 6.306/2007, Anexo | Limitação da calculadora; referência mantida |
| 4 | A calculadora cobra custódia do Tesouro Selic desde o primeiro real | 60 | R$ 14,50 | Regra oficial: isenção até R$ 10.000,00 por CPF | Limitação da calculadora; referência mantida |

Os itens 1 e 2 juntos reproduzem os dias úteis da calculadora em 132 de 132 casos (1 a 3
dias úteis a mais que a referência). Por causa deles, o RFL da calculadora fica entre
R$ 0,14 e R$ 5,13 acima do da referência no Prefixado e entre R$ 1,70 e R$ 3,46 acima no
IPCA+. No Tesouro Selic, o item 4 pesa no sentido contrário (de −R$ 11,71 a +R$ 5,30).

## 5. Reprodução

```bash
cd dados/d1-rfl/conferencia-tesouro && python3 comparar.py
```

`comparar.py` lê `api-requisicoes.json` e `api-resultados.json`, confere que a referência
reproduz o `gab_rfl_brl` de cada caso a partir das colunas de datas do `d1-casos.csv` e
grava `comparacao.csv`. Para consultar a calculadora de novo, use `consultar-api.js` no
console do navegador, na página da calculadora. As respostas podem mudar se o Tesouro
alterar a calculadora ou retirar títulos da lista.
