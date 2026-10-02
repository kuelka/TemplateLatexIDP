# Como extrair as taxas do Tesouro para o dataset D1

Roteiro para obter as taxas de Tesouro Prefixado e IPCA+ e a taxa de compra (ágio ou
deságio) do Tesouro Selic nas doze datas de aplicação do D1, sem versionar o arquivo histórico completo.

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

Foi escrito e testado contra um arquivo sintético que imita o layout e, em 23/09/2026,
rodado pelo autor sobre o arquivo real: 176.390 linhas lidas, 200 no recorte, 180
seleções. Tamanho e SHA-256 do original estão em `tesouro-PROVENIENCIA.txt`. Numa nova
execução, confira o cabeçalho impresso.

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

**Limitação constatada em 02/10/2026.** O parágrafo acima descreve o caso em que o título
vence depois do resgate. Mas a regra do vencimento mais próximo também escolhe títulos
que vencem **antes** do resgate (`gap_dias` negativo): 135 dos 360 casos de Tesouro do
estrato `calculo_rfl`, até 495 dias antes. Nesses casos não há marcação a mercado; a curva
plana equivale a supor reinvestimento à mesma taxa entre o vencimento e o resgate, com a
alíquota de IR do prazo do D1. O autor manteve a regra e declarou a limitação (ver
`README.md`). A alternativa avaliada — vencimento mais próximo igual ou posterior ao
resgate — mudaria 66 das 180 seleções e elevaria o descasamento mediano de 121 para 209
dias.

A rota descartada era ancorar os prazos nos vencimentos realmente ofertados, o que
devolveria exatidão ao Prefixado por carregamento até o vencimento, mas faria os prazos
deixarem de cair nas fronteiras de IR e IOF.

O Tesouro Selic escapa parcialmente do problema, porque é pós-fixado e o que interessa
dele é a taxa de compra sobre a Selic, não a taxa de carregamento até o vencimento.

---

## 4. Premissas — resolvidas em 02/10/2026

As três premissas que esta seção listava como abertas estão resolvidas; o registro
completo está no `README.md` e no cabeçalho do `fechar-gabarito.py`.

**Percentual do CDI para o CDB.** 94,0% do CDI: mediana dos oito últimos meses oficiais
do BCB (jun/2023–jan/2024, séries 28663 e 4391), porque as séries de taxa de CDB estão
suspensas desde 31/01/2024. Extrapolação declarada.

**Convenção de capitalização.** Não é escolha: base 252 dias úteis para a remuneração e
dias corridos para IR e IOF. Os feriados até 2029 são calculados em `rfl_referencia.py`
(Páscoa por Meeus). Continua valendo a advertência: se a convenção divergir entre o
módulo Python do objetivo (c) e a implementação de referência, a taxa de erro medida vira
artefato da divergência, não evidência sobre a H1.

**Taxa de compra do Tesouro Selic.** Sai do próprio extrato, na coluna de taxa de compra,
e entra no cálculo como `(1 + Selic efetiva) × (1 + taxa) − 1`. Taxa positiva significa
PU abaixo do valor nominal atualizado — **deságio**; negativa é **ágio**.

---

## 5. Depois

Feito em 02/10/2026: com os três extratos versionados, o `fechar-gabarito.py` chama a
**implementação de referência** (`rfl_referencia.py`) — independente do módulo Python
sob teste — e preenche `taxa_contratada_aa`, `gab_rfl_brl` e `fonte_gabarito_rfl` nos
600 casos de `calculo_rfl`. Falta a conferência amostral contra simulador oficial.
