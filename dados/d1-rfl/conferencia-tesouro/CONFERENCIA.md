# Conferência do gabarito do D1 contra a calculadora oficial do Tesouro Direto

**Data:** 02/10/2026 · **Escopo:** casos de Tesouro do estrato `calculo_rfl` · **Resultado:**
132 de 360 casos conferidos; nenhuma diferença aponta erro de cálculo em `rfl_referencia.py`.
Uma convenção de prazo ficou para decisão do autor (seção 5).

O `d1-casos.csv` **não foi alterado**. Em `fonte_gabarito_rfl`, a conferência continua
marcada como PENDENTE até a decisão da seção 5.

## 1. Fontes

| Item | Origem |
|---|---|
| Calculadora | Tesouro Direto, Calculadora avançada (`https://www.tesourodireto.com.br/simuladores/calculadora-avancada`). O próprio formulário chama `POST /o/calculadora-avancada`, e as consultas foram feitas nesse endereço. Respostas registradas entre 19:06:16 e 19:07:22 de 02/10/2026 (campo `BizSts.dtTm` da resposta) |
| Ressalva da fonte | A página avisa que os resultados são "apenas exemplificativos". A calculadora serve aqui como conferência independente da aritmética, não como valor oficial de liquidação |
| Regras do Tesouro Direto | Página "Regras e Regulamento" (`https://www.tesourodireto.com.br/sobre-o-tesouro/regras-e-regulamento`), consultada em 02/10/2026: custódia de 0,2% a.a. sobre o valor dos títulos, provisionada diariamente a partir da liquidação da compra (D+1); Tesouro Selic isento até R$ 10.000,00 por CPF; prazo do IRRF contado entre as datas de **liquidação** da aplicação e do resgate (orientação do Tesouro Nacional de 2018) |
| Calendário | ANBIMA, `https://www.anbima.com.br/feriados/arqs/feriados_nacionais.xls`, baixado em 02/10/2026, 111.104 bytes, SHA-256 `e3070152bfbdd733a27977adc82b799e973d3ea003d2aa25b0e7e5bdae63aa17`. De 2025 a 2029, os feriados batem um a um com `feriados_nacionais()` de `rfl_referencia.py` |

## 2. Amostra

Entraram **todos** os casos de Tesouro do estrato `calculo_rfl` que a calculadora aceita.
São três restrições da própria calculadora:

1. o título ainda precisa estar listado (os vencimentos de 2026 já saíram);
2. a data de resgate não pode passar do vencimento (`gap_dias` ≥ 0 em `tesouro-selecao.csv`);
3. a taxa de compra precisa ser positiva (deságio). Taxa zero ou ágio é recusada.

Em cada consulta, a taxa de venda é igual à de compra, que é a premissa de curva plana da
Rota A. A taxa da instituição financeira é zero.

| Produto | 15 | 180 | 360 | 720 | 1.080 |
|---|---|---|---|---|---|
| Tesouro Selic | 3/36 | 3/36 | 18/36 | 18/36 | 18/36 |
| Tesouro Prefixado | 10/24 | 10/24 | 12/24 | 12/24 | 12/24 |
| Tesouro IPCA+ | 0/12 | 0/12 | 0/12 | 4/12 | 12/12 |

As datas de aplicação vão de 02/06/2025 a 04/05/2026. Ficam sem cobertura o IPCA+ de 15,
180 e 360 dias (todos usam a NTN-B Principal de 15/08/2026, já vencida) e os 135 casos em
que o título vence antes do resgate. O CDB não tem simulador oficial equivalente.

## 3. O que bate

- **Aritmética da remuneração.** Com os mesmos dias úteis da calculadora, o montante bruto
  da referência difere no máximo R$ 0,04 (132 de 132).
- **Alíquota de IR:** igual em 132 de 132.
- **Base do IR:** a calculadora cobra IR sobre bruto menos aplicado, sem descontar a
  custódia. É a regra adotada em 02/10 (IN RFB nº 1.585/2015, art. 46, § 1º).
- **Valor líquido:** bruto menos IR menos custódia, a mesma ordem da referência.
- **Custódia sobre o valor atualizado** (correção de 02/10): no Prefixado e no IPCA+, a
  diferença é de centavos (máximo R$ 0,27).

## 4. Diferenças e sua origem

| # | Diferença | Casos | Efeito máximo | Origem | Tratamento |
|---|---|---|---|---|---|
| 1 | A calculadora trata 20/11 como dia útil | 48 com 20/11/2025 na janela | 1 dia útil | 20/11 é feriado nacional desde 2024 (Lei nº 14.759/2023) e consta do calendário ANBIMA | Defeito da calculadora; referência mantida |
| 2 | A calculadora não cobra IOF | 13 de 15 dias | R$ 5,95 | IOF regressivo do Decreto nº 6.306/2007, Anexo | Limitação da calculadora; referência mantida |
| 3 | A calculadora cobra custódia do Tesouro Selic desde o primeiro real | 60 | R$ 14,48 | Regra oficial: isenção até R$ 10.000,00 por CPF | Limitação da calculadora; referência mantida |
| 4 | A calculadora conta dias úteis e dias corridos a partir da **liquidação** (D+1 útil da aplicação até D+1 útil do resgate) | 132 | 1 dia útil | Orientação do Tesouro Nacional para o prazo do IRRF; custódia provisionada a partir de D+1 | **Decisão do autor** (seção 5) |

A convenção do item 4, somada ao 20/11 do item 1, reproduz os dias úteis da calculadora em
116 dos 132 casos e os dias corridos em 132 de 132. Os 16 casos restantes têm todos o resgate
num sábado, e neles a calculadora conta um dia útil a mais.

## 5. Decisão pendente do autor: prazo pela aplicação ou pela liquidação

Hoje a referência conta tudo a partir da data de aplicação: o prazo do D1 (15, 180, 360, 720
e 1.080 dias corridos) define o IR e o IOF, e os dias úteis vão da aplicação ao resgate. Para
o Tesouro, a regra oficial conta o prazo do IRRF entre as liquidações.

Efeito de adotar a liquidação nos 360 casos de Tesouro (resgate em fim de semana passa para
o dia útil seguinte):

- **IOF:** os 66 casos de 15 dias passam a ter 14 dias, e o IOF sobe de 50% para 53% do
  rendimento.
- **IR:** 54 casos mudam de faixa para baixo. São 42 casos de 180 dias que passam a 181 ou
  182 dias (22,5% → 20%) e 12 casos de 360 dias que passam a 361 (20% → 17,5%). Isso
  acontece quando o resgate cai em fim de semana.
- **RFL:** muda de −R$ 1,39 a +R$ 6,36 por caso.

Opções:

- (a) manter a data de aplicação e declarar a simplificação, sem custo de refazer nada;
- (b) adotar a liquidação só no Tesouro (como no regulamento), o que muda o gabarito de até
  360 casos e exige uma nova execução e uma nova conferência;
- (c) redefinir o prazo do D1 como prazo entre liquidações, o que mexe também no CDB e no
  texto do Capítulo 4.

## 6. Reprodução

```bash
cd dados/d1-rfl/conferencia-tesouro && python3 comparar.py
```

`comparar.py` lê `api-requisicoes.json` e `api-resultados.json`, confere que a referência
reproduz o `gab_rfl_brl` de cada caso e grava `comparacao.csv`. Para consultar a calculadora
de novo, use `consultar-api.js` no console do navegador, na página da calculadora. As
respostas podem mudar se o Tesouro alterar a calculadora ou retirar títulos da lista.
