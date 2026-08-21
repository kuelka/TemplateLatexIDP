# Bibliografia de apoio

Material de referência levantado para a dissertação, mantido aqui para consulta.
Todos os artigos abaixo já têm entrada em `referencias.bib`; os que ainda não
têm citação no corpo do texto estão marcados abaixo.

## RAG e assessoria de investimentos

- `levantamento-artigos-rag-investimentos.md`: levantamento comparativo dos três
  artigos abaixo (resumos, métricas, benchmarks e síntese de uso na dissertação).
- `artigos/kim-et-al-2025-optimizing-retrieval-strategies.pdf` — KIM, S. et al.
  *Optimizing Retrieval Strategies for Financial Question Answering Documents
  in Retrieval-Augmented Generation Systems*. KAIST, ICLR 2025 Workshop,
  arXiv:2503.15191, 2025. (chave: `kim2025`; citado na estratégia de retrieval
  híbrido, objetivo d)
- `artigos/akinfaderin-subramanian-2025-verafi.pdf` — AKINFADERIN, A.;
  SUBRAMANIAN, S. *VERAFI: Verified Agentic Financial Intelligence through
  Neurosymbolic Policy Generation*. Amazon, arXiv:2512.14744, 2025. (chave:
  `akinfaderin2025`; citado na condição de controle, objetivo e)
- `artigos/oehler-horn-2024-chatgpt-vs-robo-advisors.pdf` — OEHLER, A.; HORN, M.
  *Does ChatGPT Provide Better Advice than Robo-Advisors?* Finance Research
  Letters, v. 60, art. 104898, 2024. DOI: 10.1016/j.frl.2023.104898. (chave:
  `oehler2024`; citado como precedente metodológico do benchmark de
  suitability, objetivo e)

## Literatura adicional de RAG financeiro (levantamento 17/08/2026, ainda não citada no corpo)

Seis artigos recentes sobre retrieval-augmented generation aplicado a
question answering financeiro, levantados para aprofundar a fundamentação
da arquitetura de RAG (objetivo d) além dos três artigos da seção anterior.
Nenhum tem citação no corpo do texto ainda.

- `artigos/li-et-al-2025-fingear.pdf` — LI, Y. et al. *FinGEAR: Financial
  Mapping-Guided Enhanced Answer Retrieval*. University of Edinburgh et al.,
  arXiv:2509.12042, 2025. (chave: `li2025fingear`; citado em 04-metodologia.tex, indexação hierárquica)
- `artigos/akarsu-et-al-2026-bm25-to-corrective-rag.pdf` — AKARSU, M.;
  KARAMAN, R. K.; MIERBACH, C. *From BM25 to Corrective RAG: Benchmarking
  Retrieval Strategies for Text-and-Table Documents*. arXiv:2604.01733,
  2026. (chave: `akarsu2026`; citado em 04-metodologia.tex, busca híbrida + evitar HyDE)
- `artigos/dadopoulos-et-al-2025-metadata-driven-rag.pdf` — DADOPOULOS, M.;
  LADAS, A.; MOSCHIDIS, S.; NEGKAKIS, I. *Metadata-Driven Retrieval-Augmented
  Generation for Financial Question Answering*. arXiv:2510.24402, 2025.
  (chave: `dadopoulos2025`; citado em 04-metodologia.tex, ganho de reranking (F1-score, uma etapa) como evidência convergente)
- `artigos/lee-hong-2026-hierarchical-reranking.pdf` — LEE, J.; HONG, S.
  *Hierarchical Reranking for Scalable Financial RAG System*. Financial
  Security Institute; Hanyang University, arXiv:2607.27523, 2026. (chave:
  `lee2026`; citado em 04-metodologia.tex, reranking + evitar HyDE)
- `artigos/choe-et-al-2025-hirec-hierarchical-retrieval.pdf` — CHOE, J.;
  KIM, J.; JUNG, W. *Hierarchical Retrieval with Evidence Curation for
  Open-Domain Financial Question Answering on Standardized Documents*
  (HiREC). Hanyang University, arXiv:2505.20368, 2025. (chave:
  `choe2025hirec`; citado em 04-metodologia.tex, indexação hierárquica)
- `artigos/kobeissi-langlais-2026-decomposing-retrieval-failures.pdf` —
  KOBEISSI, A.; LANGLAIS, P. *Decomposing Retrieval Failures in RAG for
  Long-Document Financial Question Answering*. Université de Montréal/RALI,
  arXiv:2602.17981, 2026. (chave: `kobeissi2026`; citado em 04-metodologia.tex, indexação hierárquica e como contraponto ao HyDE)

## Segundo levantamento de RAG financeiro (19/08/2026)

Cinco artigos adicionais sobre RAG e LLMs aplicados ao domínio financeiro
foram enviados pelo usuário nesta rodada, avaliados um a um e triados: dois
descartados (relevância insuficiente ou incompatibilidade de desenho com o
escopo da dissertação), três incorporados ao corpo do texto.

- `artigos/mridul-et-al-2025-ai4contracts.pdf` — MRIDUL, M. A.; SLOYAN, I.;
  GUPTA, A.; SENEVIRATNE, O. *AI4Contracts: LLM & RAG-Powered Encoding of
  Financial Derivative Contracts*. Rensselaer Polytechnic Institute/South
  Cardinal, arXiv:2506.01063, 2025. (chave: `mridul2025`; citado em
  02-referencial-teorico.tex, seção RAG e Conformidade Regulatória, como
  paralelo à geração restrita a esquema do function calling — nota lateral,
  caso de uso de origem é estruturação de contratos derivativos, distinto
  do escopo desta dissertação)
- `artigos/zhu-du-2025-role-aware-multiagent-financial-education-qa.pdf` —
  ZHU, A.; DU, Y. *A Role-Aware Multi-Agent Framework for Financial
  Education Question Answering with LLMs*. Rensselaer Polytechnic
  Institute/University of Amsterdam, arXiv:2509.09727, 2025. (chave:
  `zhu2025`; citado em 04-metodologia.tex, seção da condição de controle,
  como contraponto reconhecido — o framework é inteiramente LLM, sem
  segregação de cálculo determinístico; o achado de que o ganho maior veio
  do agente de crítica, não do retrieval, é citado como direção de
  aprimoramento não explorada nesta dissertação, não como justificativa da
  arquitetura de agente único)
- `artigos/wang-et-al-2025-omnieval.pdf` — WANG, S.; TAN, J.; DOU, Z.; WEN,
  J.-R. *OmniEval: An Omnidirectional and Automatic RAG Evaluation
  Benchmark in Financial Domain*. Renmin University of China, Proceedings
  of the 2025 Conference on Empirical Methods in Natural Language
  Processing (EMNLP), p. 5726–5751, 2025. (chave: `wang2025omnieval`;
  citado duas vezes em 04-metodologia.tex — na validação da base RAG,
  como formato de avaliação da etapa de geração, e na seção de
  LLM-as-a-judge, reforçando a cautela recomendada por Bavaresco 2025 sobre
  validação humana do avaliador automático)

### Descartados

- Gimmelberg et al. 2025 (*Market Moves Predictions Using RAG Analysis of
  Capital Market Expert Opinions in Social Media*, Entrepreneurship and
  Sustainability Issues) — RAG aplicado à predição de movimento de sete
  ativos financeiros diversificados (ouro, bitcoin, S&P 500, treasuries dos
  EUA, petróleo, e as ações Tesla e Alphabet — não apenas ações, conforme
  Tabela 1 do artigo) a partir de opiniões extraídas de vídeos do YouTube. O
  abstract menciona "potencial democratizante" para o investidor de varejo,
  mas essa é a moldura retórica dos próprios autores sobre um achado de
  predição de mercado, não uma medição de redução de assimetria de
  informação em aconselhamento de renda fixa regulado — não haveria citação
  que sustente algo específico do desenho desta dissertação. PDF e entrada
  `.bib` removidos em 19/08/2026.
- Haeri et al. 2026 (*Financial Bond Similarity Search Using Representation
  Learning*, TD Bank) — embeddings de atributos categóricos para busca de
  similaridade entre um universo grande de títulos heterogêneos, uso
  institucional de modelagem de curva de spread/risco. Estruturalmente
  incompatível com a matriz de adequação produto×perfil desta dissertação
  (4 produtos fixos, não busca de similaridade). PDF e entrada `.bib`
  removidos em 19/08/2026.

## Terceiro levantamento: robo-advisors, LLMs como consultores financeiros e sistemas de recomendação (levantamento 20-21/08/2026, ainda não citado no corpo)

Dez artigos enviados pelo usuário nesta rodada (oito em 20/08/2026, mais dois
em 21/08/2026), material de contextualização sobre roboadvisors, uso de
LLMs/agentes generativos como consultores financeiros e sistemas de
recomendação em finanças — candidatos a fundamentar o referencial teórico
(Capítulo 2) e a discussão de resultados (Capítulo 6). Nenhum tem citação no
corpo do texto ainda.

### Revisão sistemática de literatura sobre robo-advisors (panorama internacional)

- `artigos/cardillo-chiappini-2024-robo-advisors-systematic-review.pdf` —
  CARDILLO, Giovanni; CHIAPPINI, Helen. *Robo-advisors: a systematic
  literature review*. Finance Research Letters, v. 62, Part A, p. 1-8,
  2024. DOI: 10.1016/j.frl.2024.105119. (chave: `cardillo2024`) — revisão
  sistemática (protocolo Scopus + Web of Science, 199 artigos
  identificados, 103 retidos após deduplicação/exclusão, período
  2017-2022, mais de 80 periódicos) que mapeia quatro correntes de
  pesquisa sobre roboadvisors: (i) classificação/tipologia -- inclui a
  tipologia de sofisticação Robo-Advisor 1.0 a 4.0 e o modelo de quatro
  tipos de Garvía (2018) (*stand-alone*, segregado, integrado,
  robo-for-advice), bem como a distinção D2C/B2B/híbrido de Phoon & Koh
  (2017); (ii) determinantes comportamentais de adoção; (iii) desempenho
  -- roboadvisors superam consultores humanos mas não batem os índices de
  mercado, com benefícios documentados para investidores
  subdiversificados, de baixa renda e baixa escolaridade, e para bancos de
  pequeno/médio porte; (iv) modelagem de algoritmo. Os autores propõem
  como agenda de pesquisa inédita uma quinta corrente -- "impacto
  socioeconômico" (inclusão financeira e efeitos sobre emprego) --
  explicitamente identificada como pouco estudada na literatura revisada.
  Relevante como referencial teórico geral para o Capítulo 2 (a tipologia
  Robo-Advisor 1.0-4.0 aqui documentada é a mesma usada por Pagan (2023,
  ver abaixo) para classificar plataformas brasileiras) e para a discussão
  do Capítulo 6: a proposta explícita dos autores de "inclusão financeira"
  como questão de pesquisa em aberto dialoga diretamente com o eixo de
  democratização da assessoria em renda fixa que motiva esta dissertação.

### Regulação e crítica de robo-advisors no Brasil

- `artigos/muniz-2025-sandbox-regulatorio-roboadvisors.pdf` — MUNIZ, José
  Matheus. *Sandbox regulatório e roboadvisors: desafios para o mercado de
  capitais*. Dissertação (Mestrado em Direito) — Faculdade de Direito de
  Ribeirão Preto, Universidade de São Paulo (FDRP/USP), Ribeirão Preto,
  2025. 133 f. Orientadora: Cristina Godoy Bernardo de Oliveira. (chave:
  `muniz2025`) — investiga se o sandbox regulatório estruturado pela CVM
  (Resolução CVM nº 29/2021) pode ser usado para regular roboadvisors no
  mercado de capitais brasileiro. Conclui que, formalmente, o sandbox atual
  não comporta roboadvisors (já operam no Brasil há anos sem vedação, não
  se qualificando como "modelo de negócio inovador"), mas que os objetivos
  e princípios do sandbox regulatório (aproximação regulador-regulado,
  proteção ao investidor, integridade de mercado, inclusão financeira,
  fomento à concorrência) justificariam a própria CVM criar um regime
  dedicado. Cita as Resoluções CVM nº 19/2021 e 21/2021 (consultoria e
  administração de carteiras) e nº 30/2021 (suitability) como o arcabouço
  regulatório vigente para roboadvisors, e reporta que roboadvisors
  brasileiros somavam quase R$1 bilhão em ativos sob gestão, com
  consolidação do setor via aquisições por grandes bancos entre 2021-2023
  (ex.: BTG-Magnetis, Nubank-Vérios/Easynvest, Santander-Toro/Monetus).
- `artigos/pagan-2023-analise-critica-roboadvisors-brasil.pdf` — PAGAN,
  João Walter Gomes. *Uma análise crítica e prática dos robo-advisors no
  mercado financeiro e de capitais brasileiro*. Dissertação (Mestrado
  Profissional em Direito dos Negócios) — Fundação Getulio Vargas, Escola
  de Direito de São Paulo (FGV-EDESP), São Paulo, 2023. 75 f. Orientador:
  Alexandre Pacheco da Silva. (chave: `pagan2023`) — pesquisa exploratória
  (revisão bibliográfica, legislativa e regulatória) sobre a estrutura,
  aspectos legais e riscos de roboadvisors no mercado brasileiro, com
  avaliação prática de plataformas nacionais anonimizadas. Desenvolve
  tipologia de sofisticação Robo-Advisor 1.0 a 4.0 e conclui que as
  plataformas brasileiras avaliadas atingem no máximo o nível 3.0 --
  ferramentas essencialmente baseadas em questionário que recomendam
  fundos proprietários da própria instituição, configurando "claro
  conflito de interesse", com deficiências de transparência (divulgação de
  código-fonte, contratos, responsabilidade civil, proteção de dados),
  embora sem evidência clara de dano ao investidor.

### LLMs e agentes generativos como consultores financeiros

- `artigos/takayanagi-et-al-2025-generative-ai-financial-advisors.pdf` —
  TAKAYANAGI, Takehiro; IZUMI, Kiyoshi; SANZ-CRUZADO, Javier; McCREADIE,
  Richard; OUNIS, Iadh. *Are Generative AI Agents Effective Personalized
  Financial Advisors?* Proceedings of the 48th International ACM SIGIR
  Conference on Research and Development in Information Retrieval (SIGIR
  2025), Padua, Italy, 2025. arXiv:2504.05862. (chave: `takayanagi2025`) —
  estudo com 64 participantes que interagiram com um LLM-consultor
  (Llama-3.1 8B) em cenários de elicitação de preferências e discussão de
  investimentos, avaliado contra preferências e rankings de referência
  definidos por especialista humano. Acurácia de elicitação de 0,70-0,85
  para dois de três perfis testados (próxima à de um consultor humano
  especialista), mas caindo a nível quase aleatório para um perfil
  "investidor de valor tolerante a risco", por "alucinação de
  preferências" (*preference hallucination*). Personalização
  bem-sucedida elevou a correlação de ranking investidor-especialista de
  0,11 para 0,31, mas quando a elicitação falhava, a personalização
  piorava ativamente os resultados (correlação negativa, até -0,286).
  Achado de risco relevante: participantes não conseguiam distinguir
  consistentemente conselho bom de ruim, e um consultor com "persona" mais
  extrovertida recebeu mais confiança/satisfação apesar de dar conselhos
  objetivamente piores.
- `artigos/fieberg-et-al-2025-llms-financial-advice.pdf` — FIEBERG,
  Christian; HORNUF, Lars; MEILER, Maximilian; STREICH, David J. *Using
  Large Language Models for Financial Advice*. CESifo Working Paper No.
  11666, Munich, jan. 2025. (chave: `fieberg2025`) — audita 32 LLMs
  (fundação vs. *fine-tuned*, por tamanho e licença) gerando
  recomendações de portfólio para 64 perfis hipotéticos de investidor
  (variando tolerância a risco, país, preferências de sustentabilidade,
  gênero, experiência), totalizando 2.048 recomendações, comparadas a 20
  dos maiores roboadvisors alemães e americanos. Acha que carteiras de LLM
  são majoritariamente implementáveis, com exposição a risco alinhada ao
  perfil declarado, e desempenho ajustado a risco comparável a
  roboadvisors (Sharpe ratio e retorno em excesso maiores, mas alfas de
  seis fatores menores -- desempenho explicado por exposição a fatores,
  não "habilidade"). Identifica viés doméstico significativo (ex.: 21 p.p.
  de sobre-alocação a ativos domésticos para investidores chineses)
  ausente nos roboadvisors de referência, mas nenhuma evidência de
  discriminação de gênero -- ao contrário da literatura sobre consultores
  humanos. Cogita explicitamente RAG como caminho promissor para injetar
  conhecimento financeiro específico sem os riscos do *fine-tuning*.
- `artigos/ross-lo-2026-heuristic-collapse-llm-investment-advice.pdf` —
  ROSS, Jillian; LO, Andrew W. *One Size Fits None: Heuristic Collapse in
  LLM Investment Advice*. Preprint, Massachusetts Institute of Technology,
  2026. arXiv:2604.23837. (chave: `ross2026`) — gera 1.000 perfis
  sintéticos de cliente (amostragem hipercubo latino) e consulta quatro
  LLMs (GPT-4o, GPT-5.4, GPT-5.4 Mini, GPT-5.4 Nano) para alocação de
  portfólio entre 20 produtos, ajustando modelos substitutos
  interpretáveis (Random Forest/Ridge) às entradas-saídas de cada modelo.
  Encontra que a tolerância a risco autodeclarada domina 57-88% do peso
  preditivo na maioria dos modelos, com idade, renda, horizonte de
  investimento e necessidade de liquidez contribuindo minimamente --
  fenômeno que os autores chamam de "colapso heurístico": conselho
  "superficialmente responsivo ao contexto, mas substantivamente
  insensível à maior parte dele". Conclui que LLMs de uso geral "não são
  consultores financeiros adequados", sendo "mais bem compreendidos como
  geradores de conselho plausível do que como fontes de recomendação
  adequada" -- forte motivação empírica para uma matriz de suitability
  determinística e calibrada por múltiplas dimensões de perfil, em vez de
  confiar a um LLM a ponderação implícita dessas dimensões.
- `artigos/vilone-et-al-2024-explainability-financial-roboadvice.pdf` —
  VILONE, Giulia; SOVRANO, Francesco; LOGNOUL, Michaël. *On the
  Explainability of Financial Robo-Advice Systems*. In: LONGO, L.;
  LAPUSCHKIN, S.; SEIFERT, C. (Eds.). Explainable Artificial
  Intelligence. Communications in Computer and Information Science, v.
  2156. Springer, 2024. p. 219-242. DOI:
  10.1007/978-3-031-63803-9_12. (chave: `vilone2024`) — extrai da
  Diretiva MiFID II e das Diretrizes ESMA sete "questões de conformidade
  legal" que uma explicação de aconselhamento financeiro automatizado
  deve responder (fontes de informação usadas, alinhamento com objetivos
  e perfil do cliente, medidas pós-hoc de adequação, grau de intervenção
  humana, ausência de conteúdo enganoso, entre outras). Testa ChatGPT 4 e
  Gemini 1.0 Pro (ferramentas de uso geral, não vinculadas legalmente ao
  MiFID II) com três personas sintéticas de investidor, verificando
  quantas das sete questões cada resposta responde. Resultado: apenas
  28% das questões foram adequadamente respondidas -- só as duas
  questões mais básicas (informação usada para o perfil do cliente e
  alinhamento geral com suas características); as três questões mais
  exigentes (fontes de informação usadas para gerar o conselho, grau de
  intervenção humana, autoavaliação de justiça/clareza/ausência de
  conteúdo enganoso) nunca foram respondidas por nenhum dos dois
  sistemas. Usa também o Flesch Reading Ease Score como métrica
  complementar de legibilidade (todas as respostas pontuaram acima de
  60, legibilidade padrão ou superior). Conclui que LLMs de uso geral têm
  potencial para gerar conselho compreensível, mas apresentam lacunas de
  transparência importantes antes de poderem ser usados em conformidade
  com o MiFID II -- evidência empírica direta, em jurisdição diferente
  (UE, não Brasil), para o mesmo tipo de risco que motiva a arquitetura
  desta dissertação (matriz de suitability determinística e módulo de
  cálculo segregado, em vez de depender do raciocínio implícito de um
  LLM).

### Sistemas de recomendação em finanças

- `artigos/zibriczky-2016-recommender-systems-meet-finance.pdf` —
  ZIBRICZKY, Dávid. *Recommender Systems meet Finance: A literature
  review*. Proceedings of the 2nd International Workshop on
  Personalization & Recommender Systems in Financial Services (FINREC
  2016), Bari, Italy, jun. 2016. CEUR Workshop Proceedings, v. 1606.
  (chave: `zibriczky2016`) — revisão de literatura (últimos 15 anos até a
  publicação) sobre sistemas de recomendação aplicados a domínios
  financeiros (banking, empréstimos, seguros, imóveis, ações, alocação de
  portfólio, venture capital, fundos), categorizando por domínio e por
  técnica (*collaborative filtering*, *content-based*,
  baseada em conhecimento, baseada em casos, métodos híbridos). Conclui
  que *collaborative*/*content-based filtering* têm
  desvantagens para domínios financeiros complexos (dificuldade de
  explicação, esparsidade de dados), enquanto métodos baseados em
  conhecimento e em casos (*case-based reasoning*) têm vantagem por
  lidarem melhor com preferências de usuário complexas e produzirem
  recomendações explicáveis -- relevante como pano de fundo teórico para
  por que a arquitetura desta dissertação prefere uma matriz de regras
  (baseada em conhecimento) a filtragem colaborativa pura.
- `artigos/sanz-cruzado-et-al-2024-fartrans-dataset.pdf` — SANZ-CRUZADO,
  Javier; DROUKAS, Nikolaos; McCREADIE, Richard. *FAR-Trans: An Investment
  Dataset for Financial Asset Recommendation*. arXiv:2407.08692, 2024.
  (chave: `sanzcruzado2024`) — dataset de uma grande instituição
  financeira europeia (clientes de varejo gregos, jan/2018-nov/2022): 806
  ativos únicos (ações, títulos e fundos, ≥200 por categoria), 703.303
  pontos de preço em 38 mercados, 29.090 clientes e 388.049 transações.
  Inclui segmento de cliente e perfil de risco MiFID II
  (Conservador/Renda/Balanceado/Agressivo). Benchmark de 11 algoritmos
  (baseados em preço, em transação/*collaborative filtering*,
  híbridos) para ranquear ativos ainda não detidos pelo cliente.
  Estruturalmente distinto da abordagem desta dissertação: é um benchmark
  de aprendizado de máquina sobre centenas de títulos individuais com
  preços variáveis e contínuos, não uma matriz de regras sobre um catálogo
  pequeno e fixo de produtos; a categoria "títulos" (*bonds*) é
  indiferenciada, sem taxonomia própria de renda fixa.

### Colaboração usuário-IA: assistente único vs. equipe de agentes especializados

- `artigos/pinhanez-et-al-2018-different-but-equal.pdf` — PINHANEZ,
  Claudio S.; CANDELLO, Heloisa; PICHILIANI, Mauro C.; VASCONCELOS,
  Marisa; GUERRA, Melina; DE BAYSER, Maíra G.; CAVALIN, Paulo. *Different
  but Equal: Comparing User Collaboration with Digital Personal Assistants
  vs. Teams of Expert Agents*. IBM Research Brazil, arXiv:1808.08157,
  2018. (chave: `pinhanez2018`) — dois estudos com usuários (69
  participantes online + 16 em laboratório) comparando um chatbot único
  ("InvestmentGuru") a uma equipe de chatbots especialistas, ambos sobre o
  mesmo sistema real "finch" de aconselhamento de investimentos de baixo
  risco em português (poupança, CDB, Tesouro). Não encontra diferença
  estatisticamente significativa em desfechos de tarefa (produto
  escolhido, confiança, competência percebida), mas encontra que a equipe
  multiagente foi mais previsível para os usuários (melhor compreensão do
  escopo de cada bot) sem custo adicional de coordenação -- nuance
  relevante para ponderar contra a opção desta dissertação por arquitetura
  de agente único, mesmo não sendo a mesma comparação (agente único +
  módulo determinístico vs. LLM sem essa segregação).

## LLM-as-a-judge (avaliação de clareza da linguagem, objetivo e)

- `artigos/zheng-et-al-2023-judging-llm-as-a-judge.pdf` — ZHENG, L. et al.
  *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*. Advances in
  Neural Information Processing Systems, v. 36, p. 46595–46623, 2023.
  arXiv:2306.05685. (chave: `zheng2023`)
- `artigos/liu-et-al-2023-g-eval.pdf` — LIU, Y. et al. *G-Eval: NLG Evaluation
  using GPT-4 with Better Human Alignment*. Proceedings of the 2023
  Conference on Empirical Methods in Natural Language Processing, p.
  2511–2522, 2023. arXiv:2303.16634. (chave: `liu2023geval`)
- `artigos/li-et-al-2024-llms-as-judges-survey.pdf` — LI, H. et al.
  *LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods*.
  arXiv:2412.05579, 2024. (chave: `li2024llmjudges`)
- `artigos/bavaresco-et-al-2025-llms-instead-of-human-judges.pdf` — BAVARESCO,
  A. et al. *LLMs instead of Human Judges? A Large Scale Empirical Study
  across 20 NLP Evaluation Tasks*. Proceedings of the 63rd Annual Meeting of
  the Association for Computational Linguistics (Volume 2: Short Papers), p.
  238–255, 2025. arXiv:2406.18403. (chave: `bavaresco2025`)

## Legibilidade textual em português (métrica de clareza, objetivo e)

Cinco artigos levantados para fundamentar a métrica de legibilidade em
português que complementa o LLM-as-a-judge na dimensão de clareza
(seção "Instrumento de avaliação de clareza -- LLM-as-a-judge" do
Anexo III, `anexo-3-instrumento-avaliacao.tex`). Todos os cinco têm
citação no corpo do texto do Anexo III.

- `artigos/martins-et-al-1996-readability-formulas-textbooks.pdf` — MARTINS,
  T. B. F.; GHIRALDELO, C. M.; NUNES, M. G. V.; OLIVEIRA JR., O. N.
  *Readability Formulas Applied to Textbooks in Brazilian Portuguese*. Notas
  do ICMSC, Série Computação, n. 28. São Carlos: Instituto de Ciências
  Matemáticas de São Carlos, USP, 1996. (chave: `martins1996readability`) —
  artigo seminal da adaptação do índice de Flesch para o português
  brasileiro: aplica a fórmula original a 120 trechos de livros didáticos
  (1ª série ao ensino superior) e propõe um deslocamento de +42 pontos na
  escala de Flesch para compensar a maior média de sílabas por palavra do
  português frente ao inglês (confirmado por comparação direta entre textos
  de física introdutória em inglês e sua tradução). Base histórica direta
  das adaptações usadas pelos demais artigos deste levantamento.
- `artigos/moreno-et-al-2023-alt-software-legibilidade.pdf` — MORENO, G. C.
  de L.; SOUZA, M. P. M. de; HEIN, N.; HEIN, A. K. *ALT: um software para
  análise de legibilidade de textos em língua portuguesa*. Policromias —
  Revista de Estudos do Discurso, Imagem e Som, Rio de Janeiro, v. 8, n. 1,
  p. 91–128, jan./abr. 2023. (chave: `moreno2023alt`) — apresenta o
  software ALT (Análise de Legibilidade Textual, disponível em
  legibilidade.com), que adapta ao português **seis** índices (Flesch
  Reading Ease, Gunning Fog, Automated Readability Index, Flesch-Kincaid
  grade level, Coleman-Liau e Índice Gulpease) e calcula um índice final
  pela média aritmética de **quatro** deles -- Gunning Fog, ARI,
  Flesch-Kincaid grade level e Coleman-Liau, todos na escala de nível de
  escolaridade. Flesch Reading Ease e Gulpease ficam de fora da média
  final (operam em escala 0-100 distinta, "centígrada") e são reportados
  separadamente. Ferramenta adotada para operacionalizar a métrica de
  legibilidade validada para o português mencionada em
  04-metodologia.tex e detalhada no Anexo III, seção de avaliação de
  clareza por LLM-as-a-judge.
- `artigos/martins-et-al-2025-fisica-moderna-ia-legibilidade.pdf` — MARTINS,
  Q. da S.; CADILLO, R. V. F.; SILVA, L. G. F. da. *Conceitos de Física
  Moderna a partir de Inteligência Artificial: uma verificação da
  legibilidade*. Revista do Professor de Física, v. 9, n. 1, p. 1–18,
  Brasília, 2025. (chave: `martins2025fisica`) — aplica o software ALT a
  respostas de ChatGPT e Copilot sobre conceitos de física moderna;
  relevante como precedente metodológico de uso do ALT para medir
  legibilidade de texto gerado por LLM (não de documento humano),
  paralelo direto ao caso de uso desta dissertação, ainda que em domínio
  de conteúdo distinto (física, não renda fixa).
- `artigos/albuquerque-santos-2025-chatgpt-readability-lisbon.pdf` —
  ALBUQUERQUE, F.; GOMES DOS SANTOS, P. *Can ChatGPT improve the
  readability of financial reporting by the public sector entities? The
  case of Lisbon municipality*. Cogent Social Sciences, v. 11, n. 1,
  2524004, 2025. DOI: 10.1080/23311886.2025.2524004. (chave:
  `albuquerque2025`) — estudo quase-experimental que usa ChatGPT (GPT-4)
  para reescrever trechos do relatório financeiro anual do município de
  Lisboa e testa a legibilidade percebida por especialistas em finanças
  do setor público; paralelo direto ao contexto de banco público desta
  dissertação, embora meça legibilidade por avaliação humana estruturada
  (survey com especialistas), não por métrica automática de português.
- `artigos/cunha-et-al-2026-linguagem-importa-legibilidade-fundos.pdf` —
  CUNHA, E. S. C. da; GALDI, F. C.; DANTAS, J. A. *A Linguagem Importa:
  Evidências da Relação entre Legibilidade e Captação de Recursos em
  Fundos de Investimento*. Anais do 26º USP International Conference on
  Accounting, São Paulo, 2026. (chave: `cunha2026`) — estudo empírico com
  214 fundos de investimento brasileiros (jan/2020–jun/2024) que mede a
  legibilidade dos regulamentos dos fundos pelos índices FOG (Gunning),
  Flesch Reading Ease e Flesch-Kincaid (estes dois últimos adaptados ao
  português com o software ALT de Moreno et al. 2023) e encontra
  associação entre regulamentos mais complexos e menor captação líquida.
  Evidência de mercado financeiro brasileiro mais próxima ao domínio
  desta dissertação (renda fixa, investidor de perfil popular) entre os
  cinco artigos deste levantamento.

## Base legal do módulo de cálculo do RFL (objetivo c, ainda não escrito)

- `base-legal-rfl.md`: levantamento das duas tabelas tributárias regressivas
  usadas pelo módulo de cálculo (IR e IOF sobre renda fixa), com texto de
  citação pronto para quando o Capítulo 5.2 for escrito.
- `normas/decreto-6306-2007-iof-compilado.pdf` — Decreto nº 6.306, de 14 de
  dezembro de 2007 (regulamenta o IOF), versão compilada oficial
  (planalto.gov.br). Art. 32 e Anexo fundamentam a tabela regressiva do IOF.
- `normas/lei-11033-2004-ir-compilado.pdf` — Lei nº 11.033, de 21 de dezembro
  de 2004, versão compilada oficial (planalto.gov.br). Art. 1º fundamenta a
  tabela regressiva do IR sobre renda fixa.

## Personas e benchmark de suitability (objetivo e, ainda não escrito)

- `literatura-suitability-benchmark.md`: investigação sobre a literatura de
  alocação de ativos por perfil de risco (Jacobs et al. 2014, Foerster et
  al. 2017, Choi 2022) como precedente metodológico do benchmark de
  suitability; conclui que a matriz produto×perfil precisa ser construída
  como contribuição original (não existe fonte pronta para o escopo desta
  dissertação), e traz o desenho técnico de risco de crédito de CDB acima
  do FGC (Índice de Basileia via IF.data + rating de agências, caso BRB
  documentado como validação).
- `perfis-anbima-personas.md`: dados demográficos e comportamentais dos
  quatro perfis do Raio X do Investidor Brasileiro 8ª edição (Sem
  Reservas, Economiza e Não Investe, Caderneta, Diversifica), extraídos da
  fonte primária, como insumo factual para a construção das fichas de
  persona do Anexo II — não substitui a decisão de síntese ainda
  pendente.
- `renda-ibge-personas.md`: faixas de renda para calibrar o campo "Renda
  familiar" das 4 personas — decis da PNAD Contínua 2025 (extremos:
  R$268 a R$9.117/mês per capita), as 6 faixas de renda domiciliar do
  Indicador Ipea de Inflação por Faixa de Renda (Carta de Conjuntura
  nº 71, Nota 30, jun/2026, valor oficial a preços de jan/2026; chave:
  `ipea2026rendafaixa`), e a metodologia final de "superávit
  financeiro" (renda média menos despesa média por classe, Tabelas 16
  e 17 da POF 2017-2018 — adotada em substituição a "variação
  patrimonial" e "aumento do ativo", ambas descartadas por limitações
  documentadas no histórico do próprio arquivo; chave: `ibge2019pof`).
  Traz também (18/08/2026) a calibração de renda da Persona 2
  (Economiza e Não Investe): R$3.456,13/mês, ancorada na Classe C
  ponderada do Critério Brasil (ABEP/CCEB 2026, ver abaixo), com
  convergência confirmada contra a faixa de renda de leve concentração
  modal do próprio perfil na ANBIMA (8ª edição, p. 31). Chaves citadas
  em 04-metodologia.tex, subseção "Calibração numérica das personas"
  — PDFs fonte arquivados em `dados/`.
- `artigos/nogami-senra-2025-como-criar-persona.pdf` — NOGAMI, V.;
  SENRA, K. B. *Como criar uma Persona: proposta de um modelo a partir
  do uso de métodos científicos de pesquisa em um projeto de
  consultoria*. Revista de Ciências da Administração, v. 27, n. 67,
  p. 1–26, 2025. DOI: 10.5007/2175-8077.2025.e98286. (chave:
  `nogamisenra2025`; citado em 04-metodologia.tex, contraste entre o
  padrão de rigor com coleta primária e a opção desta dissertação por
  triangulação de fontes públicas secundárias)

## Dados socioeconômicos de apoio (PDFs de fonte primária, fora do escopo normativo/acadêmico)

- `dados/ipea-cc71-nota30-faixas-renda-jun2026.pdf`: Carta de Conjuntura
  nº 71, Nota de Conjuntura 30 (Ipea, divulgado 17/jul/2026) — fonte da
  Tabela 4 (faixas de renda mensal domiciliar) usada em
  `renda-ibge-personas.md`.
- `dados/ibge-pof-2017-2018-primeiros-resultados.pdf`: IBGE, Pesquisa de
  Orçamentos Familiares 2017-2018, Primeiros Resultados (69 p.) — fonte
  do conceito de "variação patrimonial" e da Tabela 16 (rendimento
  médio real por classe), usados em `renda-ibge-personas.md`.
- `dados/abep-ccb-2026-alteracoes.pdf`: ABEP, *Critério de Classificação
  Econômica Brasil (CCEB) — Alterações válidas a partir de 05/02/2026*
  (base PNADC 2025) — fonte da renda média domiciliar por estrato
  socioeconômico (A a D/E) e da distribuição populacional por classe,
  usados em `renda-ibge-personas.md` para calibrar a renda da Persona 2
  (chave: `abep2026`). Conferido linha a linha nesta rodada (19/08/2026).
- `dados/anbima-datafolha-2026-raio-x-9a-edicao.pdf`: ANBIMA/Datafolha,
  *Raio X do Investidor Brasileiro — 9ª edição*, abr. 2026 (81 p.) —
  fonte do dado sobre uso de assistentes de IA como canal de
  informação sobre investimentos (9% dos investidores, à frente de
  Facebook, e-mail, TikTok e rádio), citado em `01-introducao.tex`
  (chave: `anbima2026`). Confirma também que os 4 perfis
  comportamentais (Sem Reservas 52%, Economiza 12%, Caderneta ~19%,
  Diversifica 17%) permanecem estáveis em relação à 8ª edição — mesma
  distribuição usada em `perfis-anbima-personas.md`.
- `dados/anbima-datafolha-2025-raio-x-8a-edicao.pdf`: ANBIMA/Datafolha,
  *Raio X do Investidor Brasileiro — 8ª edição*, jan. 2025 — fonte
  primária de todo o `perfis-anbima-personas.md` (chave: `anbima2025`).
  Reconferido linha a linha nesta rodada (18/08/2026): confirma
  exatamente a cifra usada como âncora de renda do João (71% das
  pessoas com renda familiar até R$1.412/mês pertencem ao Perfil Sem
  Reservas) e a quase totalidade dos demais dados dos 4 perfis. Dois
  erros de transcrição de etnia foram encontrados e corrigidos (ver
  nota de verificação no próprio arquivo).

## Corpus normativo da base RAG regulatória (objetivo d, ainda não construída)

- `normas-rag-corpus.md`: levantamento das 6 normas que compõem o corpus
  regulatório inicial (CVM 30/2021 e CMN 4.557/2017, 4.968/2021, 4.879/2020,
  4.893/2021, 5.274/2025), com conteúdo verificado diretamente contra o
  texto oficial e trecho literal do inciso XIV da CMN 5.274/2025 (monitoramento
  de Deep Web/Dark Web) já transcrito.
- `normas/resolucao-cvm-30-2021-suitability.pdf` — Resolução CVM nº 30/2021
  (dever de verificação de adequação ao perfil do cliente).
- `normas/resolucao-cmn-4968-2021-controles-internos.pdf` — Resolução CMN
  nº 4.968/2021 (sistemas de controles internos).
- `normas/resolucao-cmn-4879-2020-auditoria-interna.pdf` — Resolução CMN
  nº 4.879/2020 (atividade de auditoria interna).
- `normas/resolucao-cmn-4893-2021-seguranca-cibernetica.pdf` — Resolução CMN
  nº 4.893/2021 (política de segurança cibernética).
- `normas/resolucao-cmn-5274-2025-altera-4893.pdf` — Resolução CMN nº
  5.274/2025 (altera a 4.893/2021; 14 controles mínimos de segurança
  cibernética).
- `normas/resolucao-cmn-4557-2017-gerenciamento-riscos-capital.pdf` —
  Resolução CMN nº 4.557/2017 (gerenciamento de riscos e capital), versão
  consolidada com alterações até a Resolução CMN nº 5.194/2024.

## Normas de apoio ao Anexo III (fora do corpus RAG do objetivo d)

- `normas/resolucao-cmn-4222-2013-regulamento-fgc.pdf` — Resolução CMN nº
  4.222/2013 (estatuto e regulamento do Fundo Garantidor de Créditos —
  FGC), **versão vigente consolidada** (enviada pelo usuário em
  19/08/2026; PDF sem camada de texto, conteúdo conferido via OCR nas 39
  páginas). Usada na observação sobre CDB acima do limite do FGC, Anexo
  III (`anexo-3-instrumento-avaliacao.tex`) — não faz parte do corpus
  RAG do objetivo (d), que permanece fechado com os 6 documentos acima.
  **Achado da conferência**: o limite de R$250 mil por CPF/conglomerado
  financeiro está confirmado, inalterado. A numeração do parágrafo mudou
  desde o texto de 2013 originalmente publicado (era §3º, hoje é §2º,
  Anexo II com redação dada pela Resolução nº 4.688/2018) — sem impacto
  no texto da dissertação, que cita a resolução sem apontar parágrafo
  específico. A versão vigente também expõe, no mesmo artigo (§3º atual),
  o teto global de R$1.000.000,00 por CPF a cada 4 anos consecutivos, não
  mencionado na observação do Anexo III até o momento.
- `normas/lei-15263-2025-linguagem-simples.pdf` — Lei nº 15.263, de 14 de
  novembro de 2025. Institui a Política Nacional de Linguagem Simples nos
  órgãos e entidades da administração pública direta e indireta de todos
  os Poderes da União, dos Estados, do Distrito Federal e dos Municípios
  (chave: `lei15263`; enviada pelo usuário em 20/08/2026; PDF sem camada
  de texto -- "Print To PDF" --, conteúdo conferido via OCR nas 3
  páginas, confere com a citação já usada). Usada no limiar de aceitação
  da métrica de legibilidade, Anexo III (`anexo-3-instrumento-
  avaliacao.tex`, seção "Instrumento de avaliação de clareza") -- fonte
  do respaldo jurídico do critério, vinculante para bancos públicos como
  entidades da administração pública indireta; não estabelece valor
  numérico específico, apenas princípios e técnicas qualitativas (art.
  5º: frases em ordem direta, frases curtas, uma ideia por parágrafo,
  explicação de jargões, entre outras). Não faz parte do corpus RAG do
  objetivo (d), que permanece fechado com os 6 documentos acima.
