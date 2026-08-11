# Literatura de Suporte ao Benchmark de Suitability (Objetivo e)

**Data do levantamento:** 11/08/2026
**Uso previsto:** objetivo específico (e) — benchmark de faixas de alocação esperadas por perfil de risco, que substitui a avaliação por especialistas na dimensão de suitability. Metodologia (Seção 4.2, "Comparabilidade com a literatura") já cita esses três artigos como base do desenho, seguindo o modelo de Oehler e Horn (2024). Ainda não incorporado ao corpo da dissertação (Capítulo 5.5, `[PENDENTE]`).

---

## 1. Jacobs, Müller e Weber (2014) — fonte primária do consenso de alocação

**Citação completa:** JACOBS, H.; MÜLLER, S.; WEBER, M. How should individual investors diversify? An empirical evaluation of alternative asset allocation policies. *Journal of Financial Markets*, v. 19, p. 62-85, 2014. DOI: 10.2139/ssrn.1471955

**Texto completo obtido e conferido** (via Deutsche Nationalbibliothek, versão working paper de julho/2013 — pode diferir marginalmente da versão final publicada em 2014, mas revisão de conteúdo é a mesma). Link: https://d-nb.info/1190294958/34

**Achado que corrige o entendimento anterior**: o artigo **não fornece três faixas de alocação por perfil de risco**. A partir de revisão de literatura (recomendações de bancos/corretoras e holdings institucionais — Arshanapalli et al. 2001, Annaert et al. 2005, Brinson et al. 1986, entre outros), os autores derivam **uma única recomendação de consenso "one-size-fits-all"**: aproximadamente **60% ações / 40% renda fixa** (ou 60%/25%/15% ao incluir commodities). O artigo então demonstra, empiricamente, que estratégias heurísticas simples de alocação fixa (como esse 60/25/15) produzem ganhos de diversificação comparáveis a 11 modelos de otimização de portfólio sofisticados, tanto para diversificação internacional em ações quanto para alocação entre classes de ativos.

**Implicação para o desenho do benchmark de suitability**: as **três faixas por perfil (A/B/C)** que aparecem no Oehler & Horn (60-70%/30-40% para o perfil conservador; 40-50%/50-60% para o moderado; 10-20%/70-80% para o arrojado) **não vêm prontas do Jacobs et al. sozinho** — são uma **síntese que os próprios Oehler & Horn constroem**, combinando os três artigos (Jacobs + Foerster + Choi), usando o 60/40 do Jacobs como âncora aproximada do perfil moderado e ajustando para cima/baixo com base na literatura mais ampla sobre tolerância a risco. **Para reproduzir o benchmark na dissertação, não basta extrair uma tabela pronta do Jacobs et al. — é necessário replicar essa lógica de síntese**, não apenas citar o número de consenso isolado.

**Acesso**: texto completo já obtido (link acima, Deutsche Nationalbibliothek, acesso aberto). Alternativa SSRN (mesmo artigo, requer download manual): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1471955

## 2. Foerster, Linnainmaa, Melzer e Previtero (2017)

**Citação completa:** FOERSTER, S.; LINNAINMAA, J. T.; MELZER, B.; PREVITERO, A. Retail financial advice: does one size fit all? *The Journal of Finance*, v. 72, n. 4, p. 1441-1482, 2017. DOI: 10.1111/jofi.12514

**Papel no benchmark:** usando dados de assessores financeiros e clientes canadenses, mostra que assessores humanos exercem influência substancial na alocação de ativos dos clientes, mas com **evidência limitada de customização** — direcionam clientes para carteiras semelhantes independentemente do perfil de risco declarado. O cliente médio paga mais de 2,7% ao ano em taxas, anulando o prêmio de risco obtido com maior exposição a ativos de risco. É a evidência empírica que Oehler e Horn citam para justificar que humano-especialista não é padrão-ouro de adequação ao perfil — o mesmo argumento que sustenta, na dissertação, a substituição da avaliação por especialistas.

**Verificação:** confirmado em múltiplas fontes (Wiley, NBER, EconPapers, ResearchGate).

**Acesso:** o periódico original (Wiley) é pago, mas está disponível como **NBER Working Paper nº 20712, de acesso aberto**:
- https://www.nber.org/papers/w20712

## 3. Choi (2022)

**Citação completa:** CHOI, J. J. Popular personal financial advice versus the professors. *Journal of Economic Perspectives*, v. 36, n. 4, p. 167-192, 2022. DOI: 10.1257/jep.36.4.167

**Papel no benchmark:** compara o conselho dado pelos 50 livros de finanças pessoais mais populares contra as prescrições de modelos econômicos acadêmicos normativos (incluindo alocação de ativos). Conclui que o conselho popular frequentemente se desvia dos princípios normativos, mas nem sempre está "errado" — muitas vezes incorpora restrições comportamentais reais (força de vontade limitada) que os modelos acadêmicos ignoram. Relevante para o desenho do benchmark porque mostra que "o que a literatura recomenda" e "o que fontes populares recomendam" podem divergir de forma sistemática e documentada — um cuidado a ter ao calibrar as faixas esperadas por perfil.

**Verificação:** confirmado em múltiplas fontes (AEA, NBER, IDEAS/RePEc, JSTOR).

**Acesso:** **acesso aberto direto** — a *Journal of Economic Perspectives* é publicada em acesso aberto integral pela American Economic Association, sem paywall:
- https://www.aeaweb.org/articles?id=10.1257/jep.36.4.167
- Versão NBER Working Paper nº 30395 (também aberta): https://www.nber.org/papers/w30395

---

## 4. Reavaliação crítica — o benchmark de Jacobs/Oehler & Horn mede a dimensão errada

**Achado desta rodada (11/08/2026), a partir de conexão com decisão de escopo já fechada desde o pré-projeto**: o escopo da dissertação é Tesouro Direto (Selic, Prefixado, IPCA+) e CDB — **só renda fixa**, com LCI/LCA explicitamente excluídos. Jacobs et al. (2014) e as faixas do Oehler & Horn medem **alocação entre ações e renda fixa** (ex.: 60% ações/40% renda fixa). Essa dimensão **não existe** no escopo de vocês — não há "ações" para alocar. O benchmark de suitability não pode ser "quanto de renda fixa", tem que ser "**qual produto de renda fixa, dado o perfil**": Tesouro Selic vs. Prefixado vs. IPCA+ vs. CDB.

**Busca por fonte oficial de referência (Tesouro Nacional/ANBIMA) para essa matriz produto×perfil**: **não encontrada**. Diferente do IOF/IR (lei) e da CVM 30/Resoluções CMN (regulação), não existe ato normativo ou documento oficial que estabeleça percentuais de alocação por perfil entre os produtos de renda fixa — é território de julgamento profissional, não de norma. Buscas em fontes de mercado (planejadores financeiros, blogs de corretora) mostraram números divergentes entre si para o mesmo perfil (ex.: "conservador" variou entre 80/15/5, 50/35/15 e 30/50/20 conforme a fonte) — confirma que não há consenso nem informal a ser simplesmente adotado.

**O que existe, de forma consistente e verificável, é a caracterização qualitativa de risco de cada produto** (convergente entre Tesouro Transparente e fontes de mercado):
- **Tesouro Selic**: baixo risco de mercado (pouca oscilação de preço no curto prazo), alta liquidez diária — associado a perfil conservador/reserva de emergência
- **Tesouro Prefixado**: risco de marcação a mercado se resgatado antes do vencimento; previsibilidade apenas se levado ao vencimento
- **Tesouro IPCA+**: proteção contra inflação, mas *duration* mais elevada → maior sensibilidade a oscilações de juros no curto prazo — associado a perfil moderado/arrojado e horizonte longo
- **CDB**: risco de crédito do emissor (não soberano), liquidez variável conforme o produto específico (o CDB Salário documentado no Capítulo 5.1 tem dinâmica própria — aplicação automática, não decisão ativa)

**Implicação metodológica**: o benchmark de suitability do objetivo (e) **não pode ser extraído de uma fonte externa pronta** — precisa ser **construído como contribuição original da dissertação**, combinando (i) as três dimensões de suitability já exigidas pela CVM nº 30/2021, Art. 3º (objetivos de investimento, situação financeira, conhecimento de risco) com (ii) a caracterização qualitativa de risco por produto acima. A literatura de Jacobs/Foerster/Choi continua válida como **precedente metodológico** — legitima usar benchmark de literatura em vez de especialista ao vivo — mas **não fornece o conteúdo numérico** que o benchmark de vocês precisa. Essa construção ainda não foi feita; fica registrada aqui como pendência explícita para quando o Capítulo 5.5 for escrito.

## 5. Risco de crédito de CDB acima do limite do FGC — fonte e desenho técnico

**Contexto**: o FGC cobre até R$ 250 mil por CPF/conglomerado financeiro (teto global R$ 1 milhão a cada 4 anos). Para valores dentro desse limite, o risco de crédito do banco emissor do CDB é irrelevante para o cliente — a proteção é do fundo, não da instituição. **Acima do limite**, o risco de crédito do emissor passa a importar diretamente.

**Fonte quantitativa oficial**: portal **IF.data do Banco Central** (www3.bcb.gov.br/ifdata), que publica trimestralmente, de forma pública e gratuita, o **Índice de Basileia** de toda instituição supervisionada. Mínimo regulatório: **11%** (13% para cooperativas). Indicador quantitativo de solidez de capital, mais preciso como proxy de risco de crédito do que a segmentação prudencial S1-S5 (que mede porte, não solvência).

**Fonte qualitativa complementar — agências de rating**: Moody's, S&P, Fitch, agências nacionais. Capturam risco que um índice contábil trimestral não pega a tempo — dimensões de governança, qualidade de gestão de risco, eventos supervenientes. **Confirmado com um caso real e atual**: o índice de Basileia do próprio BRB (Relatório Pilar III, data-base jun/2025) era 13,91% [NAO VERIFICADO NESTA RODADA: nao localizei o Pilar III diretamente nesta verificacao -- confirmar contra o relatorio antes da versao final], acima do mínimo — nada alarmante nesse indicador isoladamente. Mas, no mesmo período em que esse número foi divulgado, as três agências agiam de forma muito mais severa sobre o BRB, em decorrência da exposição ao caso Banco Master: **Moody's Local Brasil** (escala nacional) rebaixou de A.br para BBB-.br em nov/2025 e, já em abr/2026, para CCC+.br, permanecendo em revisão para novo rebaixamento (rating nacional nunca foi retirado); separadamente, a **Moody's Investors Service** (escala global) **retirou** seu rating (B3/Not Prime) a pedido do BRB em dez/2025 -- são duas classificadoras/escalas distintas do mesmo grupo, não uma sequência única. **S&P** rebaixou para B-/B e depois **retirou os ratings a pedido do próprio BRB** (dez/2025); **Fitch** rebaixou de B- para CCC e manteve em Observação Negativa, citando "graves deficiências nas práticas de supervisão e gestão de riscos" [NAO VERIFICADO NESTA RODADA: a troca do "Rating de Suporte do Controlador" por "Rating de Suporte do Governo" nao foi confirmada em fonte independente -- remover ou confirmar antes da versao final]. Isso confirma, com um caso concreto, que rating captura deterioração de risco que o índice de capital sozinho não capturou a tempo.

**Princípio de desenho explícito, sem o qual esta seção estaria incompleta**: o sistema **não deve ter nenhum viés para proteger a classificação de risco de nenhuma instituição, inclusive o próprio BRB**. O propósito central do modelo, conforme a própria dissertação já define, é servir ao investidor com informação honesta — não gerenciar a reputação de nenhum banco. Isso tem uma implicação direta de desenho: **retirada de rating após sequência de rebaixamentos (como no caso do BRB) deve ser tratada como sinal de deterioração de risco, não como ausência de sinal ou motivo para recair sobre um indicador mais brando (como o Basileia isolado)**. Um desenho correto usa o **pior sinal disponível entre os indicadores existentes**, e trata retirada-após-rebaixamento como um sinal de risco elevado por si só — não como uma lacuna neutra de dado.

**Requisito de desenho — consulta dinâmica, não valor fixo**: tanto o índice de Basileia quanto o status de rating de qualquer instituição avaliada pelo sistema devem ser consultados na informação mais recente disponível no momento da recomendação, não hardcoded — a trajetória do BRB entre jun/2025 (Basileia ainda saudável) e dez/2025 (ratings rebaixados e retirados) mostra o quão rápido esse quadro pode mudar.

## 6. Pendência separada — proposta de generalização de escopo (BRB → bancos públicos)

**Registro de discussão (11/08/2026), não aplicado ao texto da dissertação.** Durante a discussão sobre categorização de risco de CDB, surgiu a proposta de remover o BRB como caso de aplicação central e reformular a dissertação como um assessor genérico para bancos públicos, "plugável" no suitability de clientes de qualquer instituição — argumento de que isso já estaria coberto por H2 (ex-H3), que promete arquitetura modular adaptável a outros bancos públicos.

**Por que isso fica registrado como pendência separada, não decidido aqui**: H2 é uma alegação sobre a *adaptabilidade* do sistema construído no BRB — não uma proposta de trocar o caso de aplicação central. Generalizar de fato tocaria título, pergunta de pesquisa, H1, referencial teórico (construído em cima da "natureza dual" *do BRB* especificamente, Costa 2016), e a calibração das personas — mudança de magnitude comparável ou maior que a remoção do H2/CEP já feita nesta dissertação. Além disso, o problema imediato que motivou a proposta (desconforto de o próprio agente do BRB indicar um CDB concorrente como mais seguro) **não deve ser resolvido escondendo ou suavizando risco real do BRB** — o propósito do sistema é servir o investidor, não proteger a instituição (ver princípio explícito na Seção 5). Se o BRB de fato apresentar risco de crédito elevado acima do limite do FGC, o sistema deve refletir isso honestamente, e essa mudança de escopo não é necessária para isso.

**Recomendação**: não aplicar essa generalização sem alinhamento explícito com o Prof. Alex, dado o tamanho do impacto estrutural.

---

## Nota metodológica

Diferente do estágio anterior — o **Jacobs et al. (2014) já foi lido por completo** e rendeu uma correção importante de entendimento (ver seção 1). Foerster et al. (2017) e Choi (2022) seguem no nível de confirmação bibliográfica robusta (citação exata confirmada em múltiplas fontes independentes), ainda não lidos por completo — ambos têm link de acesso aberto direto, prontos para leitura integral quando for útil.
