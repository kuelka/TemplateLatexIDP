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

## Segundo levantamento de RAG financeiro (19/08/2026, ainda não citada no corpo)

Cinco artigos adicionais sobre RAG e LLMs aplicados ao domínio financeiro,
enviados pelo usuário nesta rodada. Abrangem aplicações mais diversas que o
levantamento de 17/08/2026 (QA sobre documentos financeiros): predição de
mercado a partir de opiniões de especialistas, busca de similaridade entre
títulos de renda fixa, estruturação de contratos derivativos, QA multiagente
para educação financeira, e um benchmark de avaliação de RAG no domínio
financeiro. Nenhum tem citação no corpo do texto ainda — decisão de onde
(e se) encaixar cada um permanece em aberto.

- `artigos/gimmelberg-et-al-2025-market-moves-rag-social-media.pdf` —
  GIMMELBERG, D.; BELINSKIY, A.; GŁOWACKA, M.; KOROTKII, S.; ARTAMONOV, V.;
  LUDVIGA, I. *Market Moves Predictions Using Retrieval-Augmented Generation
  (RAG) Analysis of Capital Market Expert Opinions in Social Media*.
  Entrepreneurship and Sustainability Issues, v. 13, n. 1, p. 175–188, 2025.
  DOI: 10.9770/w9365778559. (chave: `gimmelberg2025`; RAG + LLM aplicado a
  predição de movimento de mercado a partir de opiniões extraídas de vídeos
  do YouTube — possível referência para a discussão de casos de uso de RAG
  em finanças além de QA regulatório)
- `artigos/haeri-et-al-2026-financial-bond-similarity-search.pdf` — HAERI,
  A.; GHELICHI, M.; AGRAWAL, N.; LI, D.; GOMEZ SANCHEZ, C. *Financial Bond
  Similarity Search Using Representation Learning*. TD Bank, Model
  Development/Risk Management, arXiv:2602.07020, 2026. (chave: `haeri2026`;
  embeddings de atributos categóricos para busca de similaridade entre
  títulos de renda fixa — não é RAG stricto sensu, mas tangencia o domínio
  de renda fixa da dissertação; relevância a confirmar)
- `artigos/mridul-et-al-2025-ai4contracts.pdf` — MRIDUL, M. A.; SLOYAN, I.;
  GUPTA, A.; SENEVIRATNE, O. *AI4Contracts: LLM & RAG-Powered Encoding of
  Financial Derivative Contracts*. Rensselaer Polytechnic Institute/South
  Cardinal, arXiv:2506.01063, 2025. (chave: `mridul2025`; RAG aplicado à
  estruturação de contratos de derivativos em formato machine-readable —
  caso de uso distinto de QA/suitability)
- `artigos/zhu-du-2025-role-aware-multiagent-financial-education-qa.pdf` —
  ZHU, A.; DU, Y. *A Role-Aware Multi-Agent Framework for Financial
  Education Question Answering with LLMs*. Rensselaer Polytechnic
  Institute/University of Amsterdam, arXiv:2509.09727, 2025. (chave:
  `zhu2025`; framework multiagente com RAG — Evidence Agent, Generator
  Agent, Expert Reviewer Agent — para QA financeiro educacional; ganho de
  6,6–8,3% sobre baseline Chain-of-Thought)
- `artigos/wang-et-al-2025-omnieval.pdf` — WANG, S.; TAN, J.; DOU, Z.; WEN,
  J.-R. *OmniEval: An Omnidirectional and Automatic RAG Evaluation
  Benchmark in Financial Domain*. Renmin University of China, Proceedings
  of the 2025 Conference on Empirical Methods in Natural Language
  Processing (EMNLP), p. 5726–5751, 2025. (chave: `wang2025omnieval`;
  benchmark de avaliação de sistemas RAG no domínio financeiro combinando
  métricas rule-based e LLM-based — possível referência metodológica para
  a avaliação da arquitetura RAG da dissertação, objetivo d/e)

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
