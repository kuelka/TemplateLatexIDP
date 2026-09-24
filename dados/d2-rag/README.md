# Dataset D2 — Perguntas normativas para validação da base RAG

**Gerado em:** 23/09/2026 · **Gerador:** `gerar-d2.py` · **Saída:** `d2-perguntas.csv` (51 itens)

Conjunto que valida a recuperação documental da base RAG regulatória (objetivo
específico *d*) **antes** da integração ao agente, permitindo calcular recall@k e
precisão sem que o desempenho do LLM contamine a medida.

## Composição

| Subconjunto | n | Função |
|---|---|---|
| `D2` | 39 | Recuperação ordinária |
| `D2b` | 12 | Vigência — dispositivos revogados, alterados, ou objeto de tentativa de alteração que não vingou |

Por categoria: suitability 22, vigência 12, governança 6, tributação 5, garantia 4,
linguagem 2. Por nível: básico 9, intermediário 18, avançado 24.

## Esquema

`id`, `subconjunto`, `categoria`, `norma`, `dispositivo`, `pergunta`, `gabarito`,
`arquivo_fonte`, `nivel`

Cada item aponta o dispositivo exato e o PDF oficial arquivado em
`bibliografia/normas/`. Os dez arquivos referenciados foram conferidos como existentes
no repositório.

## Origem dos gabaritos

Todos extraídos do texto oficial arquivado, nenhum de memória:

| Norma | Base |
|---|---|
| Res. CVM nº 30/2021 | texto consolidado com as alterações das Res. CVM nº 162/22 e 179/23 |
| Res. CMN nº 4.222/2013 | Regulamento do FGC, Anexo II |
| Lei nº 11.033/2004 e Decreto nº 6.306/2007 | tabelas de IR e IOF, já conferidas em `bibliografia/base-legal-rfl.md` |
| Lei nº 15.263/2025 | Política Nacional de Linguagem Simples |
| Res. CMN nº 4.557/2017, 4.879/2020, 4.893/2021, 4.968/2021, 5.274/2025 | corpus do objetivo *d*, conferido em `bibliografia/normas-rag-corpus.md` |

## Sobre o D2b

O subconjunto de vigência é o que dá sentido ao mecanismo de metadados da base. Os
casos mais exigentes são os do art. 11, VII e do art. 12, III da Res. CVM nº 30/2021: o
documento oficial consolidado **contém as três redações sucessivas do mesmo inciso**,
empilhadas no corpo do texto. Uma base que recupere o trecho errado responderá "agentes
autônomos de investimento" onde a redação vigente, dada pela Res. CVM nº 179/2023, diz
"assessores de investimento". É um erro silencioso, plausível e verificável — exatamente
o tipo de falha que o mecanismo de vigência existe para evitar.

O item sobre a MP nº 1.303/2025 testa a situação inversa: uma alteração amplamente
noticiada que **não** entrou em vigor. Uma base contaminada por material jornalístico
tenderá a responder que a tabela regressiva do IR foi substituída por alíquota única.

## Pendências

1. **Revisão item a item pelo autor**, antes de qualquer uso — as perguntas são proposta
   de redação, não versão final.
2. **Validação da redação com o orientador.**
3. **Dimensionamento.** O desenho registrado no documento de alinhamento de 21/08/2026
   fala em "30 a 50 perguntas"; este conjunto tem 51. Ou se exclui um item, ou se ajusta
   a redação do texto.
4. **Definição do k** de recall@k, ainda não fixada na metodologia.
