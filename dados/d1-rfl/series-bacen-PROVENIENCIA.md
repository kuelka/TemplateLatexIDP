# Séries do BACEN — proveniência

**Coletado em:** 23/09/2026, mediante autorização expressa do autor.
**Fonte:** Sistema Gerenciador de Séries Temporais (SGS) do Banco Central do Brasil,
`https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados`

| Coluna | Série SGS | Descrição | Unidade |
|---|---|---|---|
| `selic_meta_aa` | **432** | Meta Selic definida pelo Copom | % a.a. |
| `cdi_aa` | **4389** | Taxa CDI anualizada, base 252 | % a.a. |
| `ipca_12m_aa` | **13522** | IPCA acumulado em 12 meses | % |

## Regra de defasagem do IPCA

O IPCA de um mês de referência é divulgado pelo IBGE por volta do dia 10 do mês
seguinte. Como as doze datas de aplicação caem entre os dias 1 e 4, a leitura mais
recente **publicada** em cada data é sempre a do mês de referência M−2, onde M é o mês
da aplicação. A coluna `ipca_mes_referencia` registra qual mês foi usado em cada linha.

## Conferência

A extração das doze datas foi conferida contra uma segunda consulta independente ao
mesmo endpoint, em janela estreita (25/03/2026 a 10/05/2026), que retornou o conteúdo
bruto e confirmou tanto os valores quanto a data efetiva da redução da meta Selic de
14,75% para 14,50% (30/04/2026).

Trajetória da meta Selic na janela: 14,75% até 18/06/2025; 15,00% de 19/06/2025 a
18/03/2026; 14,75% de 19/03/2026 a 29/04/2026 — já refletida na leitura de 01/04/2026
—; 14,50% a partir de 30/04/2026. O CDI acompanha a meta com diferencial estável de
0,10 p.p.

## O que o SGS não fornece

O BACEN **não publica** as taxas contratadas dos títulos do Tesouro Direto. As taxas de
Tesouro Prefixado e Tesouro IPCA+ nas datas de aplicação vêm do Tesouro Transparente,
arquivo `precotaxatesourodireto.csv` (recurso CKAN
`796d2059-14e9-44e3-80c9-2d9e30b405c1`). O recurso **não tem datastore ativo**, o que
impede consulta filtrada por data — só há o arquivo completo, que precisa ser baixado e
arquivado no repositório.
