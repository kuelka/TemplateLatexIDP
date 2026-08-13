# Dados de Renda (IBGE e Ipea) para Calibração das Personas

**Data do levantamento:** 12/08/2026
**Uso previsto:** insumo factual para o campo "Renda familiar" e para a
decisão sobre a capacidade de investimento atribuída a cada persona do
`anexos/anexo-2-personas.tex` (Anexo II). **Este memo não decide o valor
final** — traz as opções de fonte primária (IBGE/PNAD Contínua e Ipea/
Carta de Conjuntura) já verificadas, para que a escolha seja feita de
forma consciente e rastreável.

---

## 1. Por que não usar direto o número do Observatório Brasileiro das Desigualdades

O valor que havíamos verificado antes (R$ 3.376, Observatório
Brasileiro das Desigualdades/Dieese, relatório de 12/ago/2026) é
essencialmente o mesmo conceito que o IBGE publica oficialmente como
**rendimento médio mensal real de todas as fontes** — o IBGE registra
R$ 3.367 para 2025 (PNAD Contínua, divulgado em 08/05/2026), a pequena
diferença provavelmente vem de base de deflação/arredondamento
distintos entre as duas publicações. Mas os dois são a mesma coisa:
**renda individual média nacional**, puxada para cima pela concentração
no topo — não é uma renda familiar, nem é específica de nenhum perfil
socioeconômico.

## 2. Opções de fonte primária (todas IBGE/PNAD Contínua 2025, divulgação 08/05/2026)

| Indicador | Valor (2025) | O que representa |
|---|---:|---|
| Rendimento médio de todos os trabalhos (individual) | R$ 3.560 | só rendimento do trabalho, pessoa ocupada |
| Rendimento médio de todas as fontes (individual) | R$ 3.367 | trabalho + aposentadoria/pensão + programas sociais etc., por pessoa com rendimento |
| **Rendimento domiciliar per capita (nacional)** | **R$ 2.264** | renda total do domicílio ÷ número de moradores -- é o conceito mais próximo de "renda familiar" per capita |
| Rendimento domiciliar per capita -- domicílios com Bolsa Família | R$ 774 | população efetivamente vulnerável, sem programa social só R$ 2.787 |
| Rendimento domiciliar per capita -- domicílios com BPC-LOAS | R$ 1.218 | idosos/pessoas com deficiência de baixa renda |
| Rendimento domiciliar per capita -- domicílios SEM nenhum programa social | R$ 2.787 | contraponto à linha acima |
| Rendimento domiciliar per capita -- Região Sudeste | R$ 2.669 | referência regional (BRB é DF, ver item 3) |

Nota metodológica do IBGE: em 2025, **os 10% mais ricos receberam, em
média, 13,8 vezes mais do que os 40% mais pobres** (rendimento
domiciliar per capita), e detinham 40,3% de toda a massa de renda --
Gini do rendimento domiciliar per capita em 0,511. Ou seja, qualquer
"média nacional" está estruturalmente distante da renda típica da
maior parte da população -- é uma média puxada por poucos.

## 3. Ponto específico para esta dissertação: BRB é Distrito Federal

O IBGE também publica rendimento domiciliar per capita por Unidade da
Federação. Levantamento anterior (rendimento domiciliar per capita
2025, divulgação 27/02/2026) mostra o **Distrito Federal com R$ 4.538**
-- quase o dobro da média nacional (R$ 2.316 nessa mesma série, que usa
metodologia de cálculo levemente diferente da série de 08/05, mas a
mesma ordem de grandeza). Isso é relevante: **as personas representam
clientes do BRB, que atua especificamente no DF** -- usar a renda
nacional (de qualquer um dos indicadores acima) pode subestimar
sistematicamente a renda real do público de referência. Não temos
ainda a decomposição do rendimento do DF por perfil ANBIMA (isso não
existe publicado; teria que ser aproximado).

## 4. Ponto 6 -- capacidade real de poupança em famílias de baixa renda

Fonte: IBGE, **Pesquisa de Orçamentos Familiares (POF) 2017-2018**
(última edição com resultados completos publicados; a POF 2024-2025
está em campo/apuração, sem microdados de despesa por classe de renda
disponíveis ainda -- se isso for crítico, posso checar de novo mais
perto da escrita final do Anexo II).

Achado direto: **famílias com renda até R$ 1.908/mês (na época da
pesquisa) destinavam 61,2% de todos os seus gastos só a alimentação e
habitação** -- sem contar transporte, saúde e outras despesas
essenciais. Esse grupo (23,9% das famílias brasileiras) contribuía com
apenas 5,5% da renda média nacional agregada.

**Isso é uma tensão real com a premissa de R$ 330/mês (10% de
R$ 3.376) de capacidade de investimento para o João**: um orçamento
familiar de baixa renda, segundo o próprio IBGE, já compromete a
maior parte do que recebe só com necessidades básicas antes de contar
qualquer outra despesa. Não invalida a simplificação -- é uma decisão
de modelagem legítima simplificar "situação financeira" para não
entrar em orçamento doméstico completo -- mas se a banca perguntar "o
IBGE mostra que famílias nessa faixa de renda mal cobrem o básico,
como o senhor justifica 10% de sobra para investir?", a resposta
precisa estar pronta.

## 5. Distribuição por décimos (o que foi pedido nesta rodada)

O índice de Gini (0,511 em 2025, ver Seção 2) é um número único que
resume o grau de desigualdade -- não traz faixas de renda. Quem traz é
a distribuição por décimos da PNAD Contínua.
O IBGE não publicou a tabela completa dos 10 décimos na divulgação de
08/mai/2026 (só os extremos, abaixo), mas são exatamente os extremos
que mais importam para calibrar Sem Reservas (base da distribuição) e
Diversifica (topo):

| Recorte | Rendimento domiciliar per capita (2025) |
|---|---:|
| **10% mais pobres (1º decil)** | **R$ 268/mês** |
| 40% mais pobres (referência agregada) | recebem, no total, 13,8× menos que os 10% mais ricos |
| 70% mais pobres (referência agregada) | detêm 32,8% de toda a massa de renda |
| Média nacional (referência) | R$ 2.264/mês |
| **10% mais ricos (10º decil)** | **R$ 9.117/mês** |
| 1% mais rico | R$ 24.973/mês |

Não encontrei a tabela oficial 2025 com os 10 décimos completos (2º a
9º) em divulgação de imprensa -- ela existe no SIDRA (sistema de
tabelas do IBGE), mas não em formato de release textual. Se for
importante ter os décimos intermediários (ex.: para Economiza e
Caderneta, que não estão nem no extremo pobre nem no rico), posso
tentar acessar o SIDRA diretamente -- avisar se vale a pena.

**Leitura direta para as 4 personas**, cruzando com o que já sabemos
do perfil comportamental de cada uma (`perfis-anbima-personas.md`):
- **Sem Reservas** (52% da população, concentrado nas faixas mais
  baixas): mais próximo do 1º decil -- **R$ 268 a R$ 774** (o teto
  sendo a média dos domicílios com Bolsa Família) é o intervalo mais
  defensável, bem mais baixo que os R$ 3.376 usados inicialmente.
- **Economiza e Não Investe** (distribuição mais equilibrada entre
  faixas de renda, pelo memo ANBIMA): mais próximo da média
  nacional, **~R$ 2.264**.
- **Caderneta** (concentração em faixas intermediárias): também
  próximo da média nacional ou um pouco acima, **R$ 2.264 a R$ 2.787**
  (usando o corte "sem programa social" como teto).
- **Diversifica** (maior concentração em classe A/B, cresce com a
  renda): mais próximo do topo da distribuição -- **R$ 9.117** (10%
  mais ricos) é defensável, ou um valor intermediário entre a média e
  esse teto, dependendo de quão "no topo" você quer que a persona
  esteja.

## 6. Faixas do IPEA (Indicador Ipea de Inflação por Faixa de Renda) -- fonte definitiva, valor oficial

**Fonte primária:** IPEA. LAMEIRAS, Maria Andreia Parente. *Inflação por
faixa de renda: junho de 2026*. Carta de Conjuntura, nº 71, Nota de
Conjuntura 30, 2º trimestre de 2026. Divulgado em 17/07/2026. Tabela 4
("Faixas de renda mensal domiciliar"), p. 3. PDF conferido e arquivado.
Metodologia: 6 faixas de renda domiciliar mensal construídas a partir
da POF 2008/2009, atualizadas pelo IPCA.

**Histórico da investigação**: a versão consultada inicialmente (Nota
de Conjuntura mais antiga da mesma edição nº 71) trazia essa tabela a
preços de maio/2020 -- desatualizada, igual ao que já aparecia na
edição nº 69 (dez/2025). A Nota 30 (divulgada em 17/jul/2026, a mais
recente da série) **já traz a tabela rebasada a preços de
janeiro/2026** -- o Ipea atualizou o apêndice metodológico entre uma
nota e outra. Isso resolve o problema: não é mais necessário estimar a
correção por IPCA, o valor é oficial e diretamente citável.

Minha estimativa anterior (fator ~1,425 sobre a base maio/2020) ficou
consistentemente ~2,3% acima do valor oficial agora disponível --
diferença pequena e na direção esperada (a estimativa mirava jul/2026;
o oficial é jan/2026, 6 meses antes). **Confirma que o método de
estimativa por IPCA estava correto**, mas o valor abaixo é o que deve
ser usado, por ser fonte primária direta, não estimativa.

### Faixas de renda mensal domiciliar -- valor oficial (preços de janeiro/2026)

| Faixa | Renda domiciliar (R$ jan./2009) | Renda domiciliar (R$ jan./2026) |
|---|---|---:|
| 1 - Renda muito baixa | Menor que R$ 900,00 | Menor que R$ 2.299,82 |
| 2 - Renda baixa | Entre R$ 900,00 e R$ 1.350,00 | Entre R$ 2.299,82 e R$ 3.449,73 |
| 3 - Renda média-baixa | Entre R$ 1.350,00 e R$ 2.250,00 | Entre R$ 3.449,73 e R$ 5.749,55 |
| 4 - Renda média | Entre R$ 2.250,00 e R$ 4.500,00 | Entre R$ 5.749,55 e R$ 11.499,11 |
| 5 - Renda média-alta | Entre R$ 4.500,00 e R$ 9.000,00 | Entre R$ 11.499,11 e R$ 22.998,22 |
| 6 - Renda alta | Maior que R$ 9.000,00 | Maior que R$ 22.998,22 |

### Leitura para as 4 personas

Essas 6 faixas cobrem o espectro completo de forma mais granular que os
extremos da PNAD Contínua (Seção 5), e são consistentes entre si (a
faixa 1 do Ipea, abaixo de R$2.299,82 domiciliar, é da mesma ordem de
grandeza do 1º decil per capita da PNAD, considerando mais de uma
pessoa por domicílio):

- **Sem Reservas**: faixa 1 ou 2 (renda muito baixa/baixa) -- até
  R$3.449,73.
- **Economiza e Não Investe**: faixa 2 ou 3 -- R$2.299,82 a R$5.749,55
  (perfil com distribuição mais equilibrada entre classes, segundo o
  memo ANBIMA).
- **Caderneta**: faixa 3 ou 4 -- R$3.449,73 a R$11.499,11 (concentração
  em faixas intermediárias).
- **Diversifica**: faixa 5 ou 6 -- acima de R$11.499,11, podendo chegar
  a faixa 6 (>R$22.998,22) se quiser representar o extremo do perfil.

## Opções para decisão (não escolhidas aqui)

1. **Manter R$ 3.376/3.367 como referência nacional**, documentando
   explicitamente que é uma simplificação didática, não uma tentativa
   de retratar a renda real do perfil Sem Reservas.
2. **Trocar para o rendimento domiciliar per capita nacional (R$ 2.264)**
   ou, melhor ainda, um valor **regionalizado para o DF**, coerente com
   o público real do BRB.
3. **Usar um valor mais baixo, ancorado no próprio perfil Sem Reservas**
   (ex.: a faixa "até R$ 1.412/mês", já documentada em
   `bibliografia/perfis-anbima-personas.md`, onde 71% das pessoas são
   Sem Reservas) -- mais realista para o perfil, mas exige revisar o
   valor de "capacidade de investimento" pra baixo também (10% de
   R$ 1.412 é só R$ 141/mês), o que pode tornar a recomendação de
   produto quase trivial (só Tesouro Selic, sem aplicação mínima
   relevante).
4. Reduzir o percentual de "capacidade de investimento" (não os 10%),
   à luz do achado da POF, e documentar a redução como decorrência
   direta do dado do IBGE.

Qualquer uma dessas é defensável — a diferença é o que cada uma
sinaliza sobre o rigor da calibração perante a banca.
