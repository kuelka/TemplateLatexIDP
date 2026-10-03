# Corpus Normativo do Objetivo (d) — Base de Conhecimento Regulatória (RAG)

**Data do levantamento:** 09-11/08/2026 (grupo A); ampliado em 02/10/2026 (grupos B e C)
**Uso previsto:** objetivo específico (d) — construção da base RAG regulatória, Capítulo 5.3 (ainda `[PENDENTE]`).
**Status:** **14 documentos**, todos com texto legível por programa (ver `bibliografia/normas/texto/PROVENIENCIA.md`;
a Res. CVM nº 30/2021 e a Res. CMN nº 4.557/2017 já têm camada de texto no PDF arquivado). Composição confirmada pelo
autor em 02/10/2026. Ainda não incorporado ao corpo da dissertação.

## Composição e justificativa

Critério de inclusão (decisão do autor, 02/10/2026): **toda regra que o agente aplica ou comunica precisa ter, no corpus,
a norma que a sustenta.** Retirar um documento deixaria uma resposta do agente sem fundamento documental rastreável.

| Grupo | Documento | Regra que sustenta | Itens no D2 |
|---|---|---|---|
| A | Res. CVM nº 30/2021 | dever de adequação ao perfil do cliente (suitability) | sim |
| A | Res. CMN nº 4.557/2017 | gerenciamento de riscos e de capital da instituição que opera o agente | sim |
| A | Res. CMN nº 4.968/2021 | controles internos | sim |
| A | Res. CMN nº 4.879/2020 | auditoria interna | sim |
| A | Res. CMN nº 4.893/2021 | política de segurança cibernética | sim |
| A | Res. CMN nº 5.274/2025 | alteração da 4.893/2021 (14 controles mínimos) | sim |
| B | Lei nº 11.033/2004 | tabela regressiva do IR | sim |
| B | Decreto nº 6.306/2007 | IOF regressivo até 30 dias (art. 32 e Anexo) | sim |
| B | Lei nº 15.263/2025 | linguagem simples na comunicação com o cidadão | sim |
| B | Res. CMN nº 4.222/2013 (Regulamento do FGC) | garantia do FGC no CDB | sim |
| C | IN RFB nº 1.585/2015 | base do IR = rendimento bruto líquido de IOF (art. 46, § 1º) | não |
| C | Regulamento do Tesouro Direto (versão de 11/10/2024) | taxa de custódia e isenção do Tesouro Selic até R$ 10.000,00 (itens 137 a 139) | não |
| C | Página "Regras e Regulamento" do Tesouro Direto | regras do TD na forma divulgada ao investidor | não |
| C | Ato Declaratório CN nº 67/2025 | MP nº 1.303/2025 com vigência encerrada em 08/10/2025 | sim (D2b-049) |

- **Grupo A:** o corpus original do objetivo (d), detalhado nos itens 1 a 6 abaixo.
- **Grupo B:** já tinham PDF arquivado em `bibliografia/normas/` e itens no D2, mas não constavam desta lista. As tabelas
  de IR e IOF estão conferidas em `bibliografia/base-legal-rfl.md`.
- **Grupo C:** entraram em 02/10/2026 (seção 7 abaixo).

**Precedência (para os metadados do passo 5).** Lei, decreto, instrução normativa e resoluções prevalecem sobre o
Regulamento do TD, e este sobre a página de Regras do TD. A página fica no corpus por ser a fonte que o investidor de fato
lê, mas contém dois erros conhecidos: diz "15% para aplicações com prazo acima de 721 dias" (a Lei nº 11.033/2004 e a
IN nº 1.585/2015 dizem acima de 720) e cita a "Instrução Normativa RFB nº 1.585/14" (é de 2015). Isso permite testar se
a base dá precedência à norma sobre o material de divulgação.

---

## 1. Resolução CVM nº 30/2021 (suitability) ✅ PDF arquivado

**Ementa:** Dispõe sobre o dever de verificação da adequação dos produtos, serviços e operações ao perfil do cliente; revoga a Instrução CVM nº 539/2013.

**Verificação: PDF oficial obtido e conferido diretamente, documento completo** (`bibliografia/normas/resolucao-cvm-30-2021-suitability.pdf` — texto consolidado com as alterações das Resoluções CVM nº 162/22 e 179/23). Confirma: Capítulos I a X, Art. 1º a 18, Anexos A e B (declarações de investidor profissional/qualificado) — sequência completa, sem lacuna. Entrada em vigor 1º/06/2021; revogação da Instrução CVM 539/2013 (Art. 17); infração grave por descumprimento dos Arts. 6º/7º (Art. 16); normas complementares por entidades autorreguladoras (Art. 15).

---

## 2. Resolução CMN nº 4.557/2017 (gerenciamento de riscos e capital)

**Ementa:** Dispõe sobre a estrutura de gerenciamento de riscos, a estrutura de gerenciamento de capital e a política de divulgação de informações (redação dada pela Resolução nº 4.745/2019).

**Verificação: texto integral obtido e conferido (45 páginas, todos os capítulos)** via fetch direto do PDF oficial. Confirma estrutura por segmento prudencial (S1-S5), RAS (Declaração de Apetite por Riscos), programa de testes de estresse, gerenciamento de risco de crédito/mercado/liquidez/operacional/social/ambiental/climático, governança (CRO, comitê de riscos).

PDF arquivado em 12/08/2026 (`bibliografia/normas/resolucao-cmn-4557-2017-gerenciamento-riscos-capital.pdf`, versão consolidada com alterações até a Resolução CMN nº 5.194/2024, 46 páginas). Link oficial:
- https://normativos.bcb.gov.br/Lists/Normativos/Attachments/50344/Res_4557_v4_P.pdf

## 3. Resolução CMN nº 4.968/2021 (controles internos) ✅ PDF arquivado

**Ementa:** Regulamenta os sistemas de controles internos das instituições financeiras e demais instituições autorizadas a funcionar pelo Banco Central do Brasil.

**Verificação: PDF oficial obtido e conferido diretamente** (`bibliografia/normas/resolucao-cmn-4968-2021-controles-internos.pdf`, versão vigente, atualizada em 29/12/2025). Confirma: Art. 1º-4º; três objetivos dos sistemas de controles internos (desempenho, informação, conformidade — Art. 3º); exclusões de âmbito de aplicação já atualizadas pela Resolução CMN nº 5.117/2024 (administradoras de consórcio, instituições de pagamento, corretoras/distribuidoras de valores mobiliários e corretoras de câmbio).

## 4. Resolução CMN nº 4.879/2020 (auditoria interna) ✅ PDF arquivado

**Ementa:** Dispõe sobre a atividade de auditoria interna nas instituições autorizadas a funcionar pelo Banco Central do Brasil.

**Verificação: PDF oficial obtido e conferido diretamente** (`bibliografia/normas/resolucao-cmn-4879-2020-auditoria-interna.pdf`, versão vigente, atualizada em 27/12/2024). Confirma: Art. 1º-3º; unidade de auditoria interna diretamente subordinada ao conselho de administração; admite auditor independente em certas condições (Art. 3º, §1º); revoga a Resolução nº 4.588/2017 e o art. 46 da Resolução nº 4.656/2018; entrou em vigor em 1º/01/2021.

## 5. Resolução CMN nº 4.893/2021 (segurança cibernética) ✅ PDF arquivado

**Ementa:** Dispõe sobre a política de segurança cibernética e sobre os requisitos para a contratação de serviços de processamento e armazenamento de dados e de computação em nuvem.

**Verificação: PDF oficial obtido e conferido diretamente** (`bibliografia/normas/resolucao-cmn-4893-2021-seguranca-cibernetica.pdf`, versão vigente, atualizada em 19/12/2025 — já incorpora a Resolução CMN nº 5.274/2025, ver item 6). Confirma: Art. 1º-3º; política de segurança cibernética deve ser compatível com porte/perfil de risco/modelo de negócio (Art. 2º, §1º); admite política única por conglomerado prudencial ou sistema cooperativo (Art. 2º, §2º); revoga as Resoluções nº 4.658/2018 e nº 4.752/2019; entrou em vigor em 1º/07/2021.

## 6. Resolução CMN nº 5.274/2025 (altera a 4.893/2021) ✅ PDF arquivado

**Ementa:** Altera a Resolução CMN nº 4.893/2021, atualizando o arcabouço de segurança cibernética.

**Verificação: PDF oficial obtido e conferido diretamente** (`bibliografia/normas/resolucao-cmn-5274-2025-altera-4893.pdf`). Datada de 18/12/2025 e publicada no DOU de 22/12/2025, em vigor na data de publicação (correção de 02/10/2026: a data de publicação vem do campo `DOU` da ficha do BCB); prazo de adequação até **1º de março de 2026** (Art. 2º).

**Achado que substitui a estimativa anterior por dado exato**: o novo Art. 3º, §2º da Resolução 4.893/2021 (redação dada pela 5.274/2025) lista, com precisão, os **14 procedimentos e controles mínimos obrigatórios** de segurança cibernética:

| # | Controle |
|---|---|
| I | Autenticação |
| II | Mecanismos de criptografia |
| III | Mecanismos de prevenção e detecção de intrusão |
| IV | Mecanismos de prevenção de vazamentos de informações |
| V | Mecanismos de proteção contra *softwares* maliciosos |
| VI | Mecanismos de rastreabilidade |
| VII | Gestão de cópias de segurança dos dados e das informações |
| VIII | Avaliação e correção de vulnerabilidades dos recursos computacionais e dos sistemas de informação |
| IX | Controles de acesso |
| X | Definição e implementação de perfis de configuração segura de ativos de tecnologia |
| XI | Mecanismos de proteção da rede |
| XII | Gestão de certificados digitais |
| XIII | Requisitos de segurança para a integração de sistemas de informação por meio de interfaces eletrônicas |
| XIV | Ações de inteligência no ambiente cibernético, **incluindo o monitoramento de informações de interesse da instituição na internet, na Deep Web e na Dark Web, além de grupos privados de comunicação** |

O item XIV é particularmente específico — vale destacar na dissertação como exemplo do nível de detalhe técnico que a base RAG regulatória precisa capturar corretamente (não é uma exigência genérica de "segurança cibernética", é um requisito nomeado e específico).

Publicada em conjunto com a Resolução BCB nº 538/2025 (mesmo tema, para instituições de pagamento/corretoras — não faz parte do escopo desta dissertação, mas fica registrado para referência).

---

## 7. Grupo C — documentos incluídos em 02/10/2026

Todos baixados das fontes oficiais em 02/10/2026; URL, data do servidor, tamanho e SHA-256 em
`bibliografia/normas/texto/PROVENIENCIA.md`.

- **IN RFB nº 1.585/2015** (`in-rfb-1585-2015-receita-api.json`): publicada no DOU de 02/09/2015, vigente. Sustenta a
  base do IR sobre o rendimento bruto deduzido do IOF (art. 46, § 1º), usada no gabarito do D1.
- **Regulamento do Tesouro Direto, versão de 11/10/2024** (`regulamento-tesouro-direto-2024-10-11.pdf`, 45 páginas,
  com camada de texto): itens 137 a 139, taxa de custódia de 0,20% a.a. e isenção do Tesouro Selic até R$ 10.000,00.
- **Página "Regras e Regulamento" do Tesouro Direto** (`tesouro-direto-regras-e-regulamento-texto.txt`): texto extraído
  no navegador, porque o site bloqueia o terminal. Precedência inferior, pelos dois erros descritos acima.
- **Ato Declaratório do Presidente da Mesa do Congresso Nacional nº 67/2025** (`ato-declaratorio-cn-67-2025-mpv-1303.htm`):
  DOU de 15/10/2025; declara encerrado em 08/10/2025 o prazo de vigência da MP nº 1.303/2025. Prova primária de que a
  alteração da tabela do IR não entrou em vigor (item D2b-049).

---

## Nota metodológica sobre profundidade de verificação

**Corpus fechado em 14 documentos.** Grupo A: 6 de 6 com conteúdo verificado diretamente contra o texto oficial e PDF
arquivado em `bibliografia/normas/` (CVM 30/2021, CMN 4.557/2017, 4.968/2021, 4.879/2020, 4.893/2021, 5.274/2025).
Grupo B: 4 de 4 com PDF arquivado e texto legível em `bibliografia/normas/texto/`. Grupo C: 4 de 4 com texto legível
em `bibliografia/normas/texto/`. A conferência dos 23 itens do D2 cujas fontes não tinham camada de texto está em
`dados/d2-rag/CONFERENCIA-TEXTOS.md`, com a verificação de vigência de 02/10/2026.
