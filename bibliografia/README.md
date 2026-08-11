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
  `oehler2024`; ainda não citado no corpo do texto)

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
- CMN nº 4.557/2017 (gerenciamento de riscos e capital): conteúdo verificado
  por fetch direto na fonte oficial, PDF ainda não arquivado localmente —
  link em `normas-rag-corpus.md`.
