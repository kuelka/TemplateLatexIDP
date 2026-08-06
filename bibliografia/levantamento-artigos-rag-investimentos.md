# Levantamento de Artigos — IA/RAG Aplicados a Investimentos

**Data da busca:** 05/08/2026
**Critério:** priorizados artigos revisados por pares ou em workshops indexados (ICLR, ACM-ICAIF), com métricas de desempenho explícitas e reprodutíveis.

# Levantamento de Artigos — IA/RAG Aplicados a Investimentos

**Data da busca:** 05/08/2026 (atualizado)
**Critério:** priorizados artigos revisados por pares ou em workshops indexados (ICLR, ACM-ICAIF), com métricas de desempenho explícitas e reprodutíveis, e maior proximidade temática/arquitetural com a proposta da dissertação (segregação cálculo determinístico × geração de linguagem, RAG regulatório, assessoria a investidor de varejo).

**Nota de versão:** esta é a segunda versão do levantamento. O Artigo 1 original (Iaroshev et al., 2024) foi substituído por dois artigos com conexão mais direta: um arquiteturalmente mais próximo (VERAFI) e um tematicamente mais próximo (Oehler & Horn, sobre assessoria de investimento). Ver histórico de decisão na conversa.

**Status de acesso:** os três PDFs completos já foram obtidos e conferidos (identidade confirmada — título, autores e DOI/arXiv ID batem). Arquivos na posse de vocês:
- `Does_ChatGPT_provide_better_advice_than_robo-advisors.pdf` (Oehler & Horn, 2024 — via CAPES/acesso institucional)
- `OPTIMIZING_RETRIEVAL_STRATEGIES_FOR_FINANCIAL.pdf` (Kim et al., 2025 — arXiv aberto)
- `VERAFI_Verified_Agentic_Financial_Intelligence_through_Neurosymbolic_Policy_Generation.pdf` (Akinfaderin & Subramanian, 2025 — arXiv aberto)

---

## Artigo 1

**KIM, S.; SONG, H.; SEO, H.; KIM, H. Optimizing Retrieval Strategies for Financial Question Answering Documents in Retrieval-Augmented Generation Systems. KAIST. Aceito no *ICLR 2025 Workshop on Advances in Financial AI*. arXiv:2503.15191, 2025.**

### 1. Resumo da abordagem
Pipeline RAG de três fases (pré-recuperação, recuperação, pós-recuperação) otimizado especificamente para documentos financeiros (10-K), incluindo: pré-processamento de consulta (expansão via LLM) e de corpus (reestruturação em markdown), *fine-tuning* de modelo de embedding (stella_en_1.5B) com dados financeiros via contrastive learning, **recuperação híbrida** (fusão ponderada densa+esparsa, com α ótimo por tipo de tarefa), reranking com cross-encoder (voyage-rerank-2), e um "agente de seleção de documentos" antes da geração, treinado por Direct Preference Optimization (DPO). Pipeline replicável publicado no GitHub.

### 2. Resultados/métricas de desempenho (dados exatos do artigo)

**Progressão do NDCG@10 ao longo do pipeline:**

| Etapa | NDCG@10 |
|---|---|
| Melhor embedding sem fine-tuning (stella 1.5B) | 0,3218 |
| Após fine-tuning financeiro (FT stella 1.5B) | 0,5086 |
| + expansão de consulta via LLM | 0,4860 |
| + reestruturação do corpus em markdown | 0,4865 |
| + reranking (voyage-rerank-2) — score final combinado | **0,5990** |

**α ótimo (peso denso vs. esparso) por dataset** — evidencia que tarefas de busca factual precisa preferem busca esparsa (α baixo), e tarefas de interpretação semântica preferem busca densa (α alto):

| Dataset | α ótimo | NDCG@10 |
|---|---|---|
| FinQABench | 0,60 | 0,9321 |
| TATQA | 0,50 | 0,9029 |
| FinanceBench | 0,85 | 0,8046 |
| ConvFinQA | 0,375 | 0,7896 |
| FinQA | 0,25 | 0,6785 |
| FinDER | 0,85 | 0,5257 |
| MultiHiertt | 0,525 | 0,2474 |

**Geração (RAGAS):** o modelo com agente de seleção + DPO (GPT-4o-mini) superou o GPT-4o puro em Answer Relevance (0,8924 vs. 0,8663) e Context Precision (0,3962 vs. 0,3418) — um modelo menor, mas com pipeline mais elaborado, supera um modelo maior sem essas camadas.

### 3. Benchmarks de RAG utilizados
Sete benchmarks financeiros nomeados, todos do FinanceRAG Challenge (Choi et al., 2024, ACM-ICAIF/Kaggle): **FinDER, FinQABench, FinanceBench (Islam et al., 2023), TATQA (Zhu et al., 2021), FinQA (Chen et al., 2021), ConvFinQA (Chen et al., 2022), MultiHiertt (Zhao et al., 2022)**. Também usa **MTEB** (Muennighoff et al., 2023) para seleção do modelo de embedding de partida — benchmark geral mais relevante para escolha de embeddings.

---

## Artigo 2

**AKINFADERIN, A.; SUBRAMANIAN, S. VERAFI: Verified Agentic Financial Intelligence through Neurosymbolic Policy Generation. Amazon. arXiv:2512.14744, 2025.**

### 1. Resumo da abordagem
O artigo parte exatamente do problema que fundamenta a dissertação de vocês: mesmo com recuperação perfeita, LLMs continuam cometendo **erros de cálculo e violações regulatórias** durante o raciocínio. A resposta é uma arquitetura que combina retrieval denso + reranking (cross-encoder) com **agentes financeiros habilitados a ferramentas — incluindo calculadoras e um ambiente de execução Python** — e uma **camada de validação neurossimbólica**: políticas de conformidade (GAAP, exigências da SEC) e validação matemática, formalmente especificadas em SMT-lib e também representadas em linguagem natural para uso em contexto pelo agente.

### 2. Resultados/métricas de desempenho
Avaliado num subconjunto no estilo FinanceBench/ConvFinQA (não o benchmark oficial completo de 150 perguntas — os autores usaram um recorte próprio com 4 empresas: American Water Works, AMD, American Express e Boeing), métrica de acurácia factual (LLM-as-a-Judge):

| Configuração | Acurácia factual | Completude |
|---|---|---|
| Apenas retrieval denso | 33,3% | 53,6% |
| + Reranking (cross-encoder) | 52,4% | 72,6% |
| + Agente com ferramentas (calculadora, Python REPL) + busca web | 90,4% | 96,4% |
| + Camada neurossimbólica (validação GAAP/SEC/matemática) | **94,7%** | 96,4% |
| **Melhoria relativa total (retrieval+rerank → completo)** | **81%** | — |

**Achado mais importante para vocês**: o salto maior não vem da camada neurossimbólica isolada (+4,3 p.p., como já destacado) — vem de **adicionar o agente com ferramentas de cálculo** (Python/calculadora) sobre o RAG puro: 52,4% → 90,4%, um salto de quase 40 pontos percentuais. Isso é evidência direta e muito forte de que a segregação cálculo×linguagem (o núcleo da arquitetura de vocês) é o componente que mais move a agulha — a camada de conformidade regulatória formal (SMT-lib, mais próxima do "RAG regulatório" de vocês) contribui a mais, mas de forma incremental sobre uma base que já melhorou muito com o cálculo determinístico.

**Detalhe arquitetural**: retrieval com Qwen3-Embedding-4B + reranking com Jina-reranker-v3; agente Claude Sonnet 4 (framework Strands) com ferramentas de calculadora, Python REPL e busca web (Tavily); mais de 80 regras de validação financeira formalizadas em SMT-lib.

### 3. Benchmarks de RAG utilizados
**Financeiro específico:** FinanceBench (Islam et al., 2023) — mesmo benchmark usado no Artigo 1, o que permite comparação direta de acurácia entre as duas abordagens. **Geral:** não utiliza RAGAS/ARES/RGB — avaliação 100% por acurácia factual no FinanceBench.

---

## Artigo 3

**OEHLER, A.; HORN, M. Does ChatGPT Provide Better Advice than Robo-Advisors? Finance Research Letters, v. 60, art. 104898, 2024.** DOI: 10.1016/j.frl.2023.104898

### 1. Resumo da abordagem
Os autores criam três perfis de investidor com diferentes tolerâncias a risco e consultam tanto o ChatGPT quanto **17 robo-advisors reais do mercado**, solicitando recomendação de carteira para cada perfil. As recomendações são comparadas contra um **benchmark derivado da literatura acadêmica** — desenho metodológico próximo ao de H1 na dissertação de vocês (comparação contra padrão de referência verificável).

**Importante:** este artigo não usa RAG — é um LLM "puro" via prompt, sem componente de recuperação de conhecimento nem cálculo determinístico separado. Serve como piso de comparação "ingênuo", não como referência arquitetural.

### 2. Resultados/métricas de desempenho
- ChatGPT alinhou-se ao benchmark acadêmico nos **três** perfis de investidor testados.
- Dos 17 robo-advisors, apenas **3** chegaram perto do benchmark nos três perfis; **3** falharam em todos.
- Conclusão dos autores: para investimentos pontuais, o ChatGPT deu conselho financeiro melhor que a maioria dos robo-advisors tradicionais baseados em regras.

### 3. Benchmarks de RAG utilizados
Nenhum — não é um sistema RAG. O "benchmark" usado é uma alocação de referência derivada da literatura de finanças pessoais (não um benchmark de RAG/IR).

---

## Síntese comparativa (atualizada)

| | Artigo 1 (Kim et al.) | Artigo 2 (VERAFI) | Artigo 3 (Oehler & Horn) |
|---|---|---|---|
| Rigor bibliográfico | Alto (workshop ICLR) | Alto (Amazon Science) | Alto (periódico peer-review) — mas pago |
| Usa RAG? | Sim | Sim | Não |
| Foco | Otimização técnica do pipeline de recuperação | Verificação matemática/regulatória sobre RAG | Qualidade da assessoria de investimento |
| Métrica principal | NDCG@10 + RAGAS | Acurácia factual (FinanceBench) | Alinhamento a benchmark de portfólio |
| Benchmark financeiro nomeado | 7 benchmarks (FinanceRAG Challenge) | FinanceBench | Benchmark próprio (literatura acadêmica) |
| Uso mais direto na dissertação | Referência técnica para construir a base RAG (objetivo d) | Evidência quantitativa central: sustenta a tese da segregação cálculo×linguagem | Evidência de que LLM supera robo-advisor tradicional; piso de comparação "sem RAG" |

