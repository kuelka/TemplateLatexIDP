# Base Legal das Tabelas Tributárias do RFL

**Data do levantamento:** 09/08/2026
**Uso previsto:** objetivo específico (c) — módulo de cálculo do Retorno Final Líquido (RFL), Capítulo 5.2 (ainda `[PENDENTE]`).
**Status:** fontes verificadas em texto oficial (planalto.gov.br); ainda não incorporado ao corpo da dissertação — só entra quando o módulo Python for de fato escrito.

---

## 1. IOF regressivo

**Base legal:** Decreto nº 6.306/2007, art. 32 e Anexo. Incide sobre o rendimento (nunca sobre o principal) em resgates de renda fixa antes de 30 dias corridos.

**Confirmado na fonte primária:** o art. 32 não tem nenhuma anotação de alteração pelos decretos de 2025 (nº 12.466, 12.467 e 12.499) — ficou de fora de toda a turbulência sobre IOF-crédito/câmbio/seguro daquele ano.

| Dia | % | Dia | % | Dia | % |
|---|---|---|---|---|---|
| 1 | 96 | 11 | 63 | 21 | 30 |
| 2 | 93 | 12 | 60 | 22 | 26 |
| 3 | 90 | 13 | 56 | 23 | 23 |
| 4 | 86 | 14 | 53 | 24 | 20 |
| 5 | 83 | 15 | 50 | 25 | 16 |
| 6 | 80 | 16 | 46 | 26 | 13 |
| 7 | 76 | 17 | 43 | 27 | 10 |
| 8 | 73 | 18 | 40 | 28 | 6 |
| 9 | 70 | 19 | 36 | 29 | 3 |
| 10 | 66 | 20 | 33 | 30+ | 0 |

**Ressalva**: o art. 32 (a regra e o gancho legal) foi confirmado diretamente no Planalto. Os 30 valores da tabela acima vêm de tabulação amplamente publicada e consistente entre fontes independentes, mas **não foram extraídos caractere a caractere do Anexo do decreto** nesta rodada (documento muito longo). Conferir os 30 valores diretamente no link abaixo antes de travar como constante no Python.

## 2. IR regressivo

**Base legal:** Lei nº 11.033/2004, art. 1º. Confirmado com o texto legal completo, sem ressalva.

| Prazo | Alíquota |
|---|---|
| Até 180 dias | 22,5% |
| 181 a 360 dias | 20% |
| 361 a 720 dias | 17,5% |
| Acima de 720 dias | 15% |

## 3. Nota de monitoramento — quase mudou em 2025

A **Medida Provisória nº 1.303/2025** tentou substituir a tabela regressiva do IR por alíquota única (a proposta oscilou entre 17,5% e 18% ao longo da tramitação). **Caducou em 8/10/2025** — a Câmara dos Deputados aprovou (251 a 193/195, conforme a fonte) a retirada de pauta da votação de conversão em lei, e a vigência se encerrou por perda de eficácia sem apreciação do Congresso (registro oficial: Atividade Legislativa MPV 1303/2025, congressonacional.leg.br) — a tabela original da Lei 11.033/2004 nunca deixou de valer. Vale registrar isso na dissertação (Limitações do estudo) como risco de desatualização a monitorar até a defesa, dado que o tema já foi objeto de tentativa legislativa séria e recente.

## 4. Links oficiais (versões compiladas, já incorporam alterações posteriores)

- Decreto nº 6.306/2007: https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6306compilado.htm
- Lei nº 11.033/2004: https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l11033compilado.htm

## 5. Texto de citação já redigido, pronto para abrir o objetivo (c) quando o módulo for escrito

> O módulo de cálculo determinístico opera sobre duas tabelas tributárias regressivas vigentes: a alíquota do Imposto de Renda sobre aplicações de renda fixa, de 22,5% a 15% conforme o prazo (Lei nº 11.033/2004, art. 1º), e a alíquota do IOF sobre resgates antes de 30 dias, de 96% a 0% sobre o rendimento (Decreto nº 6.306/2007, art. 32 e Anexo). Ambas as tabelas foram objeto de tentativa de alteração legislativa em 2025 — a Medida Provisória nº 1.303/2025 buscou substituir a tabela regressiva do IR por alíquota única, mas caducou em 8/10/2025 sem votação pelo Congresso — permanecendo, portanto, vigentes as tabelas originais na data de desenvolvimento deste módulo.
