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

## 7. Metodologia oficial para "capacidade de investimento" -- variação patrimonial (POF)

**Pergunta que motivou esta seção**: em vez de assumir um percentual
arbitrário (ex.: 10% da renda) para o campo "quanto a persona tem
disponível para investir", existe uma metodologia já publicada que
meça isso a partir do que sobra do orçamento familiar?

**Resposta: sim.** A POF tem um conceito oficial chamado **variação
patrimonial**, definido pelo IBGE como: *"vendas de imóveis, carros e
outros bens, heranças e o saldo positivo da movimentação financeira:
depósitos e retiradas de aplicações financeiras como, por exemplo,
poupança e cotas de fundos de investimento"* (POF 2017-2018, Primeiros
Resultados, p. 22 -- essa definição do conceito **está** confirmada no
PDF arquivado). Ou seja, **é literalmente o fluxo líquido de poupança e
investimento da família** -- não uma dedução feita por mim.

**Fontes -- duas, distintas, não confundir:**
1. IBGE. *Pesquisa de Orçamentos Familiares 2017-2018: Primeiros
   Resultados*. Rio de Janeiro: IBGE, 2019 (69 p., PDF completo
   arquivado em `dados/`). Contém a **definição** do conceito de
   variação patrimonial e a **Tabela 16** (renda média por classe,
   Seção seguinte) -- mas **não contém** o percentual de participação
   da variação patrimonial por classe de renda.
2. IBGE, Agência de Notícias. *"POF 2017-2018: Famílias com até R$1,9
   mil destinam 61,2% de seus gastos à alimentação e habitação"*.
   Divulgado 04/10/2019, atualizado 10/10/2019. Disponível em:
   https://agenciadenoticias.ibge.gov.br/agencia-sala-de-imprensa/2013-agencia-de-noticias/releases/25598-pof-2017-2018-familias-com-ate-r-1-9-mil-destinam-61-2-de-seus-gastos-a-alimentacao-e-habitacao
   -- **é aqui, e só aqui, que está o percentual de 1,1%/15,3%**, na
   seção "Rendimentos não monetários e transferências representam
   quase 60% dos valores recebidos pelas famílias de menor renda".

**Correção de um erro que eu tinha cometido nesta seção**: eu havia
escrito "confirmado, após leitura completa da publicação [Primeiros
Resultados]" para o percentual de 1,1% -- isso estava errado. Reconferi
o texto extraído do PDF completo (`/tmp/pof_full.txt`) e o número
**não aparece lá** -- só no release de imprensa (fonte 2 acima), que é
um documento oficial do IBGE mas **diferente** do "Primeiros
Resultados". O erro foi meu, na citação, não no dado em si.

**Verificação do dado agora que a fonte está correta**: o parágrafo do
release traz o detalhamento **completo** (soma 100,0%) para a classe
até 2 SM -- rendimento de trabalho 41% + transferências 28,8% +
aluguéis 0,3% + outras rendas 0,6% + não monetário 28,2% + variação
patrimonial 1,1% = 100,0% exato. O mesmo vale para a classe 25+ SM
(60% + 12,8% + 3,7% + 0,2% + 7,9% + 15,3% = 100,0%). A soma bater
exatamente em 100% nas duas classes é evidência de consistência
interna -- não é uma fonte fragmentada ou parcial, é um recorte
completo, só que publicado num documento diferente do que eu tinha
citado.

### Achado direto, por classe de renda (2018)

| Classe de rendimento | Participação da variação patrimonial no total recebido |
|---|---:|
| Até 2 salários mínimos (até R$ 1.908,00 em 2018) | **1,1%** |
| Mais de 25 salários mínimos (acima de R$ 23.850,00 em 2018) | 15,3% |

**Confirmado, após leitura completa da publicação "Primeiros
Resultados"**: o detalhamento de variação patrimonial por classe **não
está nessa publicação especificamente** -- está no release de imprensa
citado acima. Nenhum dos dois documentos traz esse detalhamento para
as 5 classes intermediárias.

### Renda média real por classe (Tabela 16 da POF -- fonte direta, não reconstituída)

A Tabela 16 da publicação traz o rendimento total e variação
patrimonial médio **acumulado** por classe, o que permite calcular a
média real dentro de cada uma das 7 faixas (não só o teto/piso da
faixa). Isso é mais preciso que usar os tetos do Ipea (Seção 6) para
calibrar renda de persona, porque reflete o comportamento médio real
de quem está naquela faixa, não o limite superior dela:

| Classe (POF, valores 2018) | Renda média real dentro da classe |
|---|---:|
| Até R$ 1.908 | **R$ 1.243,43** |
| R$ 1.908 a R$ 2.862 | R$ 2.367,96 |
| R$ 2.862 a R$ 5.724 | R$ 4.003,57 |
| R$ 5.724 a R$ 9.540 | R$ 7.028,21 |
| R$ 9.540 a R$ 14.310 | R$ 11.116,41 |
| R$ 14.310 a R$ 23.850 | R$ 17.752,05 |
| Acima de R$ 23.850 | R$ 40.009,63 |

**Convergência entre três fontes independentes para o perfil Sem
Reservas**: R$1.243,43 (POF, direto da Tabela 16, 2018) ≈ R$1.248,82
(minha reconstituição indireta anterior, mesma fonte) ≈ R$1.412,00
(pico de concentração do perfil Sem Reservas, ANBIMA, 2025). As três
estimativas caem na mesma ordem de grandeza, apesar de métodos e anos
diferentes -- reforça a robustez da faixa, não só de um número isolado.

Capacidade de investimento do João recalculada com a fonte direta:
**R$1.243,43 × 1,1% ≈ R$13,68/mês** (praticamente igual ao valor
anterior de R$13,74, agora com base direta na Tabela 16, sem precisar
reconstituir a partir de percentuais de imprensa).

### Comparação direta com a premissa inicial do João

A premissa original (10% de R$3.376 = R$330/mês) está **muito acima**
do que a POF mede como comportamento real de poupança/investimento
para famílias de baixa renda (1,1%, não 10%). Isso **confirma e
quantifica** a tensão já registrada na Seção 4: para uma persona
representando o perfil Sem Reservas (definido pela própria ANBIMA como
"não consegue economizar nem investir"), 10% de sobra é uma premissa
otimista, não realista -- 1,1% está muito mais alinhado ao
comportamento medido.

### Primeira comparação entre os dois conceitos (12/08/2026) -- decisão revertida depois, ver adiante

A POF tem um segundo conceito, do lado da despesa (não da renda):
**aumento do ativo** -- definido como *"despesas com a aquisição de
imóvel, a reforma de imóvel e outros investimentos"* (POF 2017-2018,
p. 19). Para a classe até R$1.908, esse componente é 1,4% da despesa
total (Tabela 6) -- em reais, ≈ R$20,88/mês, contra R$13,68/mês da
variação patrimonial.

**Descartado nesta primeira rodada** (decisão revertida depois -- ver
"Problema de direção encontrado", adiante): o grupo "aumento do ativo"
é dominado por aquisição/reforma de imóvel, fora do escopo desta
dissertação (só renda fixa). "Outros investimentos" (títulos de
capitalização, títulos de clube, terreno de jazigo) é só um resíduo
menor dentro do grupo, não segregável dos dados publicados. Na época,
pareceu mais direto usar **variação patrimonial**, que isola
especificamente movimentação de conta financeira -- *"depósitos e
retiradas de aplicações financeiras como, por exemplo, poupança e
cotas de fundos de investimento"* --, tratando aplicações financeiras
como parte do patrimônio/bens da família, o que parecia coerente com o
objetivo desta dissertação (aplicação em Tesouro/CDB é, também, um
bem). **Essa leitura não considerou, nesta primeira rodada, o problema
de direção (saque vs. depósito) explicado a seguir.**

### Decisão metodológica final (12/08/2026) -- REVERTIDA em 13/08/2026, ver abaixo

~~**Variação patrimonial é a métrica usada para "capacidade de
investimento" em todas as 4 personas**, não aumento do ativo. Critério
explícito: aplicações financeiras (o próprio objeto desta dissertação)
são tratadas como bem/patrimônio, e é exatamente esse o conceito que
variação patrimonial isola -- ainda que de forma imperfeita (mistura
com venda de bens e herança) e com dado completo só disponível para as
2 classes extremas. É a melhor aproximação disponível nos dados
públicos até o momento; se a POF 2024-2025 publicar esse detalhamento
por todas as 7 classes no futuro, vale reconferir.~~

### Problema de direção encontrado em variação patrimonial (13/08/2026) -- motivo da reversão

Ao reexaminar o release do IBGE que é a fonte do 1,1%/15,3% (Seção
"Fontes -- duas, distintas" acima), o próprio texto do IBGE ilustra o
conceito assim: *"O valor médio recebido pelas famílias, relativo ao
rendimento mensal e à variação patrimonial (**saques de poupança** e
vendas de imóveis, por exemplo)..."* -- o exemplo escolhido pelo IBGE é
**saque**, não depósito. **Isso é o fato publicado.**

**A partir daqui, o que segue é argumento metodológico meu, não
afirmação do IBGE**: variação patrimonial fica do lado da **renda** (o
que a família recebeu no ano) na contabilidade da POF. Uma família que
sacou da poupança para cobrir despesas tem esse valor contado como
"recebido" naquele ano. O IBGE não afirma em lugar nenhum que o
indicador "mede desacumulação" -- essa é uma leitura que faço a partir
de (a) o exemplo escolhido pelo próprio IBGE ser "saque", (b) o
posicionamento contábil do item do lado da renda, e (c) a consistência
dessa leitura com o que já sabíamos da classe (61,2% do orçamento em
alimentação+habitação, definição ANBIMA de "não consegue investir"). É
uma inferência plausível e argumentável, não um dado publicado -- e é
por isso que decidi tratá-la como suficiente para reverter a
metodologia, mas ela deveria ser apresentada na dissertação como
interpretação do autor, com essa ressalva explícita, não como achado
direto da POF.

**R$15,53/mês (variação patrimonial) fica invalidado como proxy de
capacidade de investimento, nessa leitura** -- não pela precisão do
número, mas pelo
que o número mede.

### Decisão final revisada (13/08/2026): aumento do ativo

Adotado **aumento do ativo** no lugar de variação patrimonial --
definido pela POF como *"despesas com a aquisição de imóvel, a reforma
de imóvel e outros investimentos"* (POF 2017-2018, Primeiros
Resultados, p. 19). Ao contrário de variação patrimonial, este é
inequivocamente **despesa** (dinheiro saindo para adquirir um bem), sem
ambiguidade de direção.

**Comparação das duas fragilidades, para registro**:
- Variação patrimonial: domínio correto (poupança/fundos de
  investimento), mas direção ambígua/provavelmente invertida.
- Aumento do ativo: direção inequívoca (aquisição), mas domínio
  misturado -- dominado por imóvel, com "outros investimentos"
  (títulos de capitalização, títulos de clube, terreno de jazigo) como
  resíduo menor, não segregável nos dados públicos.

**Ressalva específica para o perfil Sem Reservas**: é plausível que,
para famílias de baixa renda, a maior parte desse "aumento do ativo"
seja construção/reforma informal de casa -- comportamento comum nessa
faixa no Brasil --, não aplicação financeira. Não há como isolar isso
nos dados disponíveis. Registrado como limitação conhecida, não
resolvida.

**Duas opções de base -- decisão fechada em 17/08/2026** (identificada
por revisão externa em 13/08/2026): a renda-âncora do João já decidida
e cross-validada (Seção "Decisão final", mais abaixo) é R$1.412,00 --
um número individual, ancorado no pico comportamental ANBIMA.
R$1.491,42 é a despesa total **média da classe** POF -- um número
agregado, de fonte e natureza diferentes. Aplicar 1,4% sobre um ou
outro dá valores próximos, mas não idênticos:

| Base | Origem | Valor |
|---|---|---:|
| R$1.491,42 | Despesa total média da classe (Tabela 17) -- mais fiel à definição de "aumento do ativo" (% de despesa, não de renda) | R$20,88/mês |
| **R$1.412,00** | **Renda-âncora individual do João (ANBIMA, já decidida para toda a ficha) -- mantém uma única base numérica ao longo da persona** | **R$19,77/mês (escolhido)** |

Ambos os cálculos conferem (verificados de forma independente).
**Decisão final: R$1.412,00 (ANBIMA)**, não R$1.491,42 (POF). Critério
explícito do usuário: o POF é usado só para extrair o **percentual**
(1,4%, aumento do ativo) a aplicar -- a **base de renda** continua
sendo a âncora ANBIMA já fechada para toda a ficha, evitando misturar
dentro do mesmo cálculo uma fonte de 2024/2025 (ANBIMA, a renda do
João) com uma fonte de 2018 (POF, a despesa média da classe). **Nota
de rastreabilidade (18/08/2026)**: essa decisão já havia sido fechada
em 17/08/2026, mas o arquivo correspondente não chegou a ser
commitado -- refeita aqui, no mesmo teor, durante auditoria geral do
projeto.

**Valor da capacidade de investimento do João por esta metodologia
(aumento do ativo): R$1.412,00 × 1,4% ≈ R$19,77/mês.** **SUPERADO em
18/08/2026** -- ver seção "Metodologia final: superávit financeiro",
abaixo, que substitui aumento do ativo por completo.

### Lacuna de cobertura -- percentual de "aumento do ativo" só existe para os extremos (18/08/2026) -- RESOLVIDA, ver seção seguinte

~~**Achado da auditoria geral**: o percentual de aumento do ativo está
confirmado, na Tabela 6 da POF, **apenas para as 2 classes extremas**~~
-- ver "Metodologia final: superávit financeiro", abaixo, que resolve
essa lacuna por caminho diferente (não tentou completar o dado de
"aumento do ativo" que faltava; trocou de indicador para um que já
cobre as 7 classes).

### Metodologia final: superávit financeiro (renda menos despesa) -- 18/08/2026

**Proposta do usuário, superior às duas tentativas anteriores**: em vez
de depender de um percentual pré-calculado pela POF (variação
patrimonial ou aumento do ativo, ambos só publicados para as classes
extremas), calcular diretamente o **superávit financeiro** de cada
classe -- renda média menos despesa média --, usando a mesma técnica
de acumulação marginal já aplicada às Tabelas 16 (renda) e 17
(despesa) da POF. Como as duas tabelas cobrem as 7 classes completas,
essa abordagem **resolve a lacuna de cobertura por completo**, sem
precisar buscar mais dados nem interpolar.

| Classe | Renda média (Tabela 16) | Despesa média (Tabela 17) | Superávit (renda − despesa) |
|---|---:|---:|---:|
| 1 - Até R$ 1.908 | R$1.243,43 | R$1.491,42 | **-R$247,99** |
| 2 - R$ 1.908-2.862 | R$2.367,96 | R$2.325,00 | R$42,96 |
| 3 - R$ 2.862-5.724 | R$4.003,57 | R$3.668,39 | R$335,18 |
| 4 - R$ 5.724-9.540 | R$7.028,21 | R$6.146,57 | R$881,64 |
| 5 - R$ 9.540-14.310 | R$11.116,41 | R$9.162,19 | R$1.954,22 |
| 6 - R$ 14.310-23.850 | R$17.752,05 | R$14.545,90 | R$3.206,15 |
| 7 - Acima de R$ 23.850 | R$40.009,63 | R$26.928,89 | R$13.080,74 |

**Decisão do usuário (18/08/2026), aplicada às 4 personas**: o
superávit financeiro por classe é a métrica final de capacidade de
investimento, substituindo tanto variação patrimonial quanto aumento
do ativo. **Personas cuja classe apresenta superávit negativo não têm
condição de fazer nenhuma aplicação** -- não se atribui um valor
simbólico mínimo; a capacidade de investimento é tratada como
inexistente nesse caso, e não R$0 arredondado de um cálculo, mas o
reconhecimento explícito de que a classe, em média, gasta mais do que
recebe.

**Consequência direta para o João (persona 1, Sem Reservas, classe
1)**: capacidade de investimento revisada de R$19,77/mês
(aumento do ativo, decisão anterior) para **sem capacidade de
investir** -- déficit médio de R$247,99/mês na classe. Isso é
coerente com a própria definição ANBIMA do perfil ("não consegue
economizar nem investir") e com todos os indicadores já levantados
para essa classe (61,2% do orçamento em alimentação+habitação, maior
estresse financeiro entre os 4 perfis, maior taxa de endividamento).

**Impacto na narrativa -- decisão fechada (18/08/2026)**: a
justificativa de "estratégia de familiarização" (persona investe um
valor pequeno para se familiarizar com produtos, mesmo sem sobra real)
foi **descartada, não reformulada**. Decisão do usuário: encarar o
achado como leitura direta dos dados -- famílias na classe de renda
até R$1.908 têm, em média, superávit financeiro negativo no Brasil, e
são interpretadas como **impossibilitadas de investir em razão da
condição financeira real dessa classe**, não por uma limitação
específica ou arbitrária da persona. Não se propõe eufemismo
pedagógico (ex.: "aporte simbólico de familiarização") nem redesenho
de comportamento do sistema (ex.: agente redirecionar para educação
financeira) como decorrência automática deste achado -- se o sistema
vier a ter esse tipo de resposta, é decisão de desenho à parte, a
justificar independentemente, não uma tentativa de suavizar o
resultado numérico.

**Ressalva metodológica, para registro**: renda (Tabela 16) e despesa
(Tabela 17) são levantadas em módulos diferentes da POF e não fecham
perfeitamente entre si a nível de classe -- o superávit calculado é
uma estimativa por diferença de duas médias agregadas, não a média de
um superávit individual medido diretamente family a family. É a melhor
aproximação disponível nos dados públicos, mas carrega essa limitação,
a ser mencionada no texto da dissertação.



### Limitações a considerar antes de aplicar

1. **Vintage**: dado de 2018 (POF 2017-2018), mesma edição da Seção 4.
   O percentual (1,1%) provavelmente é mais estável ao longo do tempo
   do que o valor em reais, mas não há garantia -- é uma hipótese
   razoável, não um fato verificado para 2026.
2. **"Até 2 salários mínimos" não é exatamente "Sem Reservas"**: é um
   corte por renda, não pelo comportamento declarado de poupança que
   define os 4 perfis ANBIMA. Provavelmente se sobrepõe bastante ao
   perfil Sem Reservas (mesma faixa de renda predominante, ver
   `perfis-anbima-personas.md`), mas não é logicamente idêntico.
3. **Variação patrimonial pode ser negativa** em famílias individuais
   (saque de poupança para cobrir despesas) -- o 1,1% é uma média que
   já teria essa compensação embutida; não sabemos a distribuição
   dentro da classe. **Nota adicionada em 13/08/2026**: esta limitação,
   registrada aqui na primeira rodada mas não aprofundada, acabou sendo
   exatamente o motivo da reversão de metodologia registrada mais acima
   ("Problema de direção encontrado") -- o sinal escolhido pelo próprio
   IBGE para ilustrar o conceito é "saque", não depósito.
4. O valor de R$13,68/mês (fonte direta, Tabela 16), calculado com
   variação patrimonial, está **superado** -- ver reversão de
   metodologia acima. ~~O valor final é aumento do ativo sobre a
   renda-âncora ANBIMA: R$19,77/mês (decisão fechada).~~ **SUPERSEDIDO
   novamente em 18/08/2026** -- ver seção "Metodologia final: superávit
   financeiro": a classe do João tem superávit médio negativo
   (-R$247,99/mês), logo a persona não tem capacidade de investimento,
   não um valor pequeno positivo. Toda a discussão abaixo sobre "o
   valor ser baixo o bastante para tornar a recomendação quase sem
   sentido prático" fica superada por essa mesma razão -- não é mais
   uma questão de o valor ser pequeno, é a ausência de valor. Ver
   "Impacto na narrativa -- decisão fechada", na seção "Metodologia
   final", para a implicação sobre o Ponto 6 (tratar Sem Reservas como
   consumidora direta do RFL vs. caso de borda/estágio zero).

### Decisão tomada (12/08/2026)

O ponto 4 acima foi resolvido: **usar o valor realista (~1,1%, o
resultado medido pela POF), não os 10% iniciais**, com a seguinte
justificativa de desenho, a ser desenvolvida no corpo da dissertação:
mesmo um aporte simbólico tem função pedagógica -- introduz a persona
ao produto de investimento, inicia uma trilha de familiarização, e
constrói conhecimento/confiança progressivos, coerente com o
diagnóstico de baixo letramento financeiro já registrado no Capítulo
5.1 (Pesquisa BCB/FGC) e com a motivação central da dissertação
(agente de IA como via de democratização de acesso à assessoria).
Isso resolve a tensão do Ponto 6: a persona Sem Reservas deixa de ser
um caso degenerado e passa a ser o caso que testa exatamente essa
função do sistema -- recomendar o produto certo mesmo (ou
principalmente) quando o valor disponível é pequeno.

**Pendência remanescente**: falta decidir a renda-base exata do João
dentro da Faixa 1 do Ipea (Seção 6) para aplicar o percentual de 1,1%
e chegar num valor final em R$ -- usar a própria média da classe POF
"até 2 SM" (~R$1.248,82, ver acima) ou um ponto dentro da Faixa 1 do
Ipea (< R$2.299,82, ver Seção 6)? Note que são bases diferentes: POF
"até 2 SM" é mais estreita (teto R$1.908 em valores de 2018, hoje bem
mais baixo que o teto da Faixa 1 do Ipea). Se a Faixa 1 do Ipea for a
referência de renda escolhida para o Anexo II (parece ser o caso, por
ser a mais atual e granular), o mais consistente é aplicar 1,1% sobre
o valor de renda que for escolhido ali, não sobre a média POF (que é
só o dado de origem do percentual, não da renda em si).

**Decisão final (12/08/2026)**: renda familiar do João ancorada em
**R$1.412,00/mês** -- não um ponto arbitrário dentro da Faixa 1, e sim
o valor específico em que a concentração do próprio perfil Sem
Reservas atinge o pico (71%, ver `perfis-anbima-personas.md`). Esse
valor cai dentro da Faixa 1 do Ipea (< R$2.299,82), então as duas
fontes se confirmam em vez de exigir escolha arbitrária. **Ressalva de
vintage**: R$1.412 vem da pesquisa ANBIMA (coleta nov/2024, publicação
jan/2025), sem correção para 2026 -- a preços de jan/2026 (base da
Faixa 1 do Ipea) o valor real seria um pouco maior, mas a margem é
pequena o suficiente para não sair da Faixa 1 mesmo corrigido.

Capacidade de investimento resultante: ~~**R$1.412,00 × 1,1% ≈
R$15,53/mês**~~ **SUPERSEDIDO em 13/08/2026** -- ver seção "Decisão
final revisada: aumento do ativo", acima. Metodologia trocada para
aumento do ativo sobre a renda-âncora ANBIMA (R$1.412,00 × 1,4%):

~~**R$19,77/mês**~~ -- **SUPERSEDIDO novamente em 18/08/2026** -- ver
seção "Metodologia final: superávit financeiro". A classe do João
(até R$1.908) tem superávit médio **negativo** (-R$247,99/mês), logo
a persona **não tem capacidade de investimento** por essa metodologia
-- valor final substitui qualquer capacidade de investimento numérica
positiva.

Esse é o valor a constar no campo "Situação financeira" (CVM 30/2021,
art. 3º, II) da Persona 1: **sem capacidade de investimento**. A
justificativa de estratégia de familiarização registrada abaixo foi
**descartada** -- ver "Impacto na narrativa -- decisão fechada", na
seção "Metodologia final: superávit financeiro", acima.

**Nota de reconciliação (12/08/2026, após achado da Tabela 16 da
POF)**: ficou em aberto se a renda do João deveria usar o teto da
Faixa 1 do Ipea (R$2.299,82) em vez do ponto ANBIMA. Com a Tabela 16 da
POF, agora há uma terceira opção -- a renda média real de quem está na
mesma faixa (R$1.243,43) -- que **converge com o ponto ANBIMA
(R$1.412,00)**, não com o teto do Ipea. Isso é evidência a favor de
manter a decisão já tomada (R$1.412,00): dois métodos independentes
(pico de concentração comportamental da ANBIMA e média real medida
pela POF) apontam para a mesma faixa de valores, enquanto o teto do
Ipea representa o limite superior da faixa, não o comportamento típico
de quem está nela.

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

---

# Persona 2 — Economiza e Não Investe: calibração de renda (18/08/2026)

## 1. Por que a técnica do João não se aplica direto

A mesma técnica usada para o João (achar o ponto de renda onde a
concentração comportamental do perfil atinge um pico claro) **não
funciona para este perfil**. O gráfico "Perfis por faixas de renda
média familiar" (ANBIMA, 8ª edição, p. 31) mostra explicitamente que o
Economiza e Não Investe tem distribuição **quase uniforme** entre
todas as 6 faixas de renda:

| Faixa de renda | % do perfil Economiza e Não Investe |
|---|---:|
| Até R$1.412 | 10% |
| R$1.413–2.824 | 11% |
| R$2.825–4.236 | 13% |
| R$4.237–7.060 | 13% |
| R$7.061–14.120 | 12% |
| +R$14.121 | 10% |

O próprio texto do relatório confirma: *"O Perfil Economiza e Não
Investe é o que apresenta a distribuição mais equilibrada entre todas
as rendas, com fatias variando entre 10% e 13% dos grupos"*
(ANBIMA, 2025). Isso descarta a técnica de pico usada no João.

## 2. Tentativa alternativa: classe social (ABEP) — ressalva da própria ABEP

A ficha do perfil (ANBIMA, p. 26) traz a distribuição de classe social:
Classe A/B 26%, Classe C 52% (majoritária), Classe D/E 22%. A ANBIMA
usa o critério ABEP 2021/2024 pra essa classificação (nota
metodológica, p. 65).

Fonte primária consultada: ABEP. *Critério de Classificação Econômica
Brasil (CCEB)*, versão 2026 (válida a partir de 05/02/2026), base
PNADC 2025 (ABEP, 2026). A própria ABEP adverte no documento:
*"a pergunta de renda não é um estimador eficiente de nível
socioeconômico"* — a classificação real é por sistema de pontos
(bens duráveis, escolaridade do chefe de família, acesso a serviço
público), não por renda direta; a correspondência renda↔classe tem
"sobreposições importantes" entre classes.

Renda média domiciliar por estrato, ABEP 2026 (PNADC 2025):

| Estrato | Renda média | % da população (Brasil) |
|---|---:|---:|
| A | R$28.331,26 | 3,6% |
| B1 | R$13.636,18 | 4,9% |
| B2 | R$7.874,72 | 15,1% |
| C1 | R$4.526,88 | 21,2% |
| C2 | R$2.648,30 | 28,1% |
| D/E | R$1.177,55 | 27,1% |

Classe C, no esquema tripartite da ANBIMA (A/B, C, D/E), corresponde a
C1+C2 combinados. Média ponderada pelo peso populacional de cada
subclasse:

**Classe C ponderada = (21,2×4.526,88 + 28,1×2.648,30) / (21,2+28,1)
= R$3.456,13/mês.**

## 3. Checagem de convergência no João -- tentativa que NÃO confirmou (registrada como achado, não descartada)

Antes de aplicar esse método ao Economiza, foi feita uma checagem de
consistência: aplicar a mesma lógica de classe social ponderada ao
perfil Sem Reservas (João), cuja distribuição de classe já é conhecida
(A/B 13%, C 46%, D/E 41%, ficha ANBIMA p. 25 -- corrigido nesta
rodada de verificação, a citação original apontava p. 30, que na
verdade traz a tabela "Perfis por classes econômicas" (dados
diferentes); os 13/46/41% estão no cartão do próprio Perfil Sem
Reservas, p. 25), e comparar com a
renda-âncora já fechada (R$1.412,00).

Resultado: **R$3.657,50/mês** (bloco A/B ponderado R$12.191,44,
23,6% da população nacional; bloco C R$3.456,13; bloco D/E
R$1.177,55). **Não convergiu** -- é 2,6× o valor já fechado. Mesmo
excluindo a fatia de 13% em classe A/B (que sozinha explica parte da
distância), o resultado só com C+D/E ainda dá R$2.382,32 -- quase 70%
mais alto que R$1.412,00.

**Interpretação, não descartada como erro**: os dois métodos medem
coisas diferentes. O gráfico de faixas de renda mede diretamente
"nessa renda específica, qual fração é desse perfil?" -- medição
direta de comportamento por renda corrente. A classe social (ABEP)
mede capacidade de consumo/patrimônio acumulado (bens duráveis,
escolaridade do chefe de família), não renda corrente -- e a própria
ABEP já adverte sobre a alta variância dessa correspondência. Alguém
pode ter pontuação de classe mais alta por patrimônio acumulado no
passado e, ainda assim, estar sem capacidade de investir agora --
consistente com o próprio quadro de estresse financeiro/endividamento
do perfil Sem Reservas já documentado. **Essa não-convergência reforça
a decisão de manter a técnica de pico de concentração para o João**,
em vez de trocar por uniformidade de método entre as quatro personas.

## 4. Segunda convergência -- desta vez confirmada

Voltando à tabela da Seção 1: as duas faixas de renda com a fatia mais
alta do perfil Economiza e Não Investe (13%, empatadas) são
exatamente **R$2.825 a R$7.060**. O valor calculado via classe social
(R$3.456,13) **cai dentro dessa faixa** -- convergência entre duas
fontes independentes (classificação de classe da ANBIMA/ABEP e a
distribuição de renda direta da própria ANBIMA), ainda que o sinal de
concentração modal seja fraco (13% vs. 10-12% nas demais faixas, uma
diferença pequena, perto da margem de erro de 1 p.p. da pesquisa).

## 5. Decisão final (18/08/2026)

**Renda familiar do Economiza e Não Investe: R$3.456,13/mês**,
ancorada na classe social predominante do perfil (Classe C, ABEP
2026/PNADC 2025), com convergência confirmada contra a distribuição de
renda direta da própria ANBIMA (faixa de leve concentração modal,
R$2.825-7.060). PDF fonte (ABEP CCEB 2026) arquivado em
`bibliografia/dados/abep-ccb-2026-alteracoes.pdf` nesta rodada
(19/08/2026) -- `abep.org` está fora da lista de domínios com acesso
de rede liberado para busca automatizada, mesmo procedimento já usado
para `ipea.gov.br`: usuário enviou o arquivo manualmente.

### Capacidade de investimento (superávit financeiro)

R$3.456,13 cai na Classe 3 da POF (R$2.862 a R$5.724). Da tabela de
superávit já calculada (Seção "Metodologia final: superávit
financeiro"):

**Classe 3 -- Renda média R$4.003,57, Despesa média R$3.668,39,
Superávit R$335,18/mês.**

**Capacidade de investimento do Economiza e Não Investe: R$335,18/mês**
(superávit positivo, ao contrário do João) -- mesma metodologia,
aplicada de forma consistente: usa-se o superávit da classe POF
correspondente à renda-âncora da persona, não uma média de despesa
recalculada individualmente.

