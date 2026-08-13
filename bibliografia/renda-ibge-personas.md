# Dados de Renda (IBGE) para Calibração das Personas

**Data do levantamento:** 12/08/2026
**Uso previsto:** insumo factual para o campo "Renda familiar" e para a
decisão sobre a capacidade de investimento atribuída a cada persona do
`anexos/anexo-2-personas.tex` (Anexo II). **Este memo não decide o valor
final** — traz as opções de fonte primária IBGE já verificadas, para que
a escolha seja feita de forma consciente e rastreável.

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
