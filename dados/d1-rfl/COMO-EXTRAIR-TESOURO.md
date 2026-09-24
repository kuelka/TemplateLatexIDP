# Como extrair as taxas do Tesouro para o dataset D1

Roteiro para obter as taxas de Tesouro Prefixado e IPCA+ e o ágio/deságio do Tesouro
Selic nas doze datas de aplicação do D1, sem versionar o arquivo histórico completo.

---

## 1. Baixar

Arquivo (série histórica completa, dezenas de MB):

```
https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/precotaxatesourodireto.csv
```

Página do conjunto, se preferir a interface:

```
https://www.tesourotransparente.gov.br/ckan/dataset/taxas-dos-titulos-ofertados-pelo-tesouro-direto
```

Metadados, que descrevem o significado de cada coluna — baixe também, é a fonte citável
do layout:

```
https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/1a8eb2e3-4902-4a38-a1eb-6410f23d90de/download/taxa.pdf
```

**Não coloque o CSV completo no Git.** Deixe-o fora do repositório (ou em `.gitignore`) e
versione apenas os extratos gerados no passo seguinte.

## 2. Rodar o extrator

```bash
cd dados/d1-rfl
python3 extrair-tesouro.py ~/Downloads/precotaxatesourodireto.csv
```

Só biblioteca padrão do Python — sem pandas, sem instalação.

Ele produz três arquivos, todos pequenos e versionáveis:

| Arquivo | Conteúdo |
|---|---|
| `tesouro-12datas.csv` | todas as linhas dos títulos do escopo nas doze datas de aplicação — o extrato auditável |
| `tesouro-selecao.csv` | um título escolhido por (data, tipo, prazo): o de vencimento mais próximo do horizonte, com o descasamento em dias |
| `tesouro-PROVENIENCIA.txt` | SHA-256 do arquivo original, tamanho, data da extração, URL da fonte, encoding e contagens |

O script **imprime o cabeçalho que encontrar** e aborta com mensagem clara se faltar
alguma coluna esperada. Se o layout divergir, ajuste o dicionário `COLUNAS` no topo do
arquivo e rode de novo; nada mais precisa mudar.

Ele foi testado contra um arquivo sintético que imita o layout, não contra o arquivo
real — que não é acessível do ambiente onde foi escrito. Confira o cabeçalho impresso na
primeira execução.

**Títulos com juros semestrais ficam de fora de propósito.** As variantes NTN-F e NTN-B
com cupom são descartadas: o escopo são os títulos de fluxo único, e incluí-las quebraria
a correspondência com a matriz de adequação do Anexo III.

---

## 3. O problema do vencimento — leia antes de calcular

O D1 define prazos de 15, 180, 360, 720 e 1.080 dias, porque são eles que cruzam as
fronteiras das alíquotas de IR e IOF. Mas **o Tesouro não vende títulos com prazo
arbitrário**: vende títulos com data de vencimento fixa, e há poucos vencimentos
disponíveis em cada data.

O resultado é que quase nunca existe um título que vença exatamente no horizonte
desejado. O script escolhe o vencimento mais próximo e reporta o descasamento em dias,
justamente para que o tamanho do problema fique visível. Espere descasamentos de muitos
meses em vários casos.

**Decisão tomada em 23/09/2026: Rota A.**

Os prazos de 15, 180, 360, 720 e 1.080 dias permanecem como definidos, e a taxa do
título de vencimento mais próximo é usada como aproximação da taxa para aquele
horizonte, **sob premissa declarada de curva plana no intervalo**. As fronteiras
tributárias ficam intactas e o desenho do experimento não muda.

O custo dessa escolha precisa estar escrito na metodologia, não subentendido: como o
resgate ocorre antes do vencimento do título, há marcação a mercado, de modo que o RFL
do Prefixado **deixa de ser exato e passa a depender da premissa de curva plana**. O
descasamento em dias entre vencimento e horizonte, que o extrator reporta, é a medida
do tamanho dessa aproximação e deve ser informado junto com os resultados.

A rota descartada era ancorar os prazos nos vencimentos realmente ofertados, o que
devolveria exatidão ao Prefixado por carregamento até o vencimento, mas faria os prazos
deixarem de cair nas fronteiras de IR e IOF.

O Tesouro Selic escapa parcialmente do problema, porque é pós-fixado e o que interessa
dele é o ágio ou deságio sobre a Selic, não a taxa de carregamento até o vencimento.

---

## 4. Premissas a declarar

Depois da extração, faltam três declarações para o gabarito do RFL poder ser calculado.

**Percentual do CDI para o CDB.** Não é dado público. Ou se adota 100% do CDI como
referência neutra, simples e transparente, ou se levantam as taxas praticadas pelos
bancos públicos no varejo e se ancora nelas, o que é mais forte mas exige fonte citável.

**Convenção de capitalização.** Os prazos do D1 estão em dias corridos, porque é assim
que IR e IOF incidem, mas renda fixa no Brasil remunera em dias úteis, base 252. O
cálculo precisa das duas contagens, e a conversão exige o calendário de feriados da
ANBIMA **até 2029** — os prazos de 1.080 dias partindo de 2026 terminam lá. Essa é a
premissa com maior consequência: se ela divergir entre o módulo Python do objetivo (c) e
a implementação de referência do gabarito, a taxa de erro medida pelo experimento vira
artefato da divergência, não evidência sobre a H1.

**Ágio ou deságio do Tesouro Selic.** Sai do próprio extrato, na coluna de taxa de
compra. Só precisa ser declarado como tal.

---

## 5. Depois

Com os três extratos versionados e as premissas declaradas, o que falta é a
**implementação de referência** do cálculo do RFL — obrigatoriamente independente do
módulo Python sob teste, conferida por amostragem contra simuladores oficiais. Ela
preenche as colunas `taxa_contratada_aa`, `gab_rfl_brl` e `fonte_gabarito_rfl` do
`d1-casos.csv`.
