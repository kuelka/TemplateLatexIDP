# Textos das normas para a base RAG — procedência

Baixados em 02/10/2026 para a etapa (d). Os PDFs de `bibliografia/normas/` continuam como registro de época, mas
8 dos 10 não têm camada de texto: o conteúdo foi gravado como desenho vetorial, e o tachado que marca a
redação revogada também. Estes arquivos são as mesmas normas, nas mesmas fontes oficiais, em formato legível
por programa. Gravados byte a byte como o servidor os entregou, sem edição.

Planalto acessado pelo terminal com identificador de navegador (sem ele, a conexão expira). O BCB respondeu
direto. "Data do servidor" é o cabeçalho HTTP `Date` da resposta (UTC).

| Arquivo | Norma | Conteúdo | Origem | Data do servidor (UTC) | Bytes | SHA-256 |
|---|---|---|---|---|---|---|
| `lei-11033-2004-compilado.htm` | Lei nº 11.033/2004 | texto compilado (vigente), mesma fonte do PDF arquivado | `https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l11033compilado.htm` | 02/10/2026 23:08:10 | 61802 | `da73ef76016c72fec78cb822fe4e52f53d690cf903de8b2f15b17cf687114fb6` |
| `lei-11033-2004-com-redacoes-anteriores.htm` | Lei nº 11.033/2004 | texto com as redações anteriores tachadas (<strike>) | `https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l11033.htm` | 02/10/2026 23:08:11 | 114062 | `5ae536c7499f52206f630dda71276ced8b7ed380e7307da57c909756fd77fdad` |
| `decreto-6306-2007-compilado.htm` | Decreto nº 6.306/2007 | texto compilado (vigente), mesma fonte do PDF arquivado | `https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6306compilado.htm` | 02/10/2026 23:08:11 | 267402 | `0d00c9fc1d52ae1fa869d618ee9c32b33af021a157a6ed964a8666d1301c9419` |
| `decreto-6306-2007-com-redacoes-anteriores.htm` | Decreto nº 6.306/2007 | texto com as redações anteriores tachadas (<strike>) | `https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6306.htm` | 02/10/2026 23:08:11 | 550965 | `3cd120b72dada919a130ec1b9316e331fc2aadafd9fcc8a51d8437d9f23b284b` |
| `lei-15263-2025.htm` | Lei nº 15.263/2025 | texto original | `https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15263.htm` | 02/10/2026 23:08:12 | 23755 | `071d6df3766de7a9df32e6b63c28ae27c07d72e43b02c0d02d811d2a98be6b57` |
| `resolucao-cmn-4222-2013-v19-vigente.pdf` | Res. CMN nº 4.222/2013 (Regulamento do FGC) | versão 19, só a redação vigente (sufixo _L); inclui a Res. CMN nº 5.295/2026 | `https://normativos.bcb.gov.br/Lists/Normativos/Attachments/48942/Res_4222_v19_L.pdf` | 02/10/2026 23:09:15 | 418578 | `f5296b4783433a065f8a128fe1f3e57973bc7cb00a63dbc550834f5b700bcd92` |
| `resolucao-cmn-4222-2013-v19-com-redacoes-anteriores.pdf` | Res. CMN nº 4.222/2013 (Regulamento do FGC) | versão 19 com as redações anteriores empilhadas (sufixo _P) | `https://normativos.bcb.gov.br/Lists/Normativos/Attachments/48942/Res_4222_v19_P.pdf` | 02/10/2026 23:09:16 | 720952 | `d4f78cf866d9b52fd40c3dab253fbb12fd7e813d0862acbc61bf0b07969f6110` |
| `resolucao-cmn-4222-2013-bcb-api.json` | Res. CMN nº 4.222/2013 | ficha do normativo: lista de versões e de atualizações; o campo Texto traz a redação original de 2013 | `https://www.bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Resolu%C3%A7%C3%A3o&p2=4222` | 02/10/2026 23:08:56 | 75445 | `d94f2c38e955001c4d345e5eeead43b58ee90307bc5d962b82e4823a0ebd382b` |
| `resolucao-cmn-4879-2020-bcb-api.json` | Res. CMN nº 4.879/2020 | ficha e texto (campo Texto, HTML); redações anteriores tachadas (<s>) | `https://www.bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Resolu%C3%A7%C3%A3o%20CMN&p2=4879` | 02/10/2026 23:08:35 | 42984 | `ccc05262757647ee266da6d26351eb66618b6fbb5c6c06de12f08be8bcab1479` |
| `resolucao-cmn-4893-2021-bcb-api.json` | Res. CMN nº 4.893/2021 | ficha e texto (campo Texto, HTML), já com as alterações da Res. CMN nº 5.274/2025; redações anteriores tachadas (<s>) | `https://www.bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Resolu%C3%A7%C3%A3o%20CMN&p2=4893` | 02/10/2026 23:08:36 | 113528 | `41df2464fb41227d559a3e3f7bf6271d2689fb8be9cbbf43a46b0a5ad587eb1d` |
| `resolucao-cmn-4968-2021-bcb-api.json` | Res. CMN nº 4.968/2021 | ficha e texto (campo Texto, HTML); redações anteriores tachadas (<s>) | `https://www.bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Resolu%C3%A7%C3%A3o%20CMN&p2=4968` | 02/10/2026 23:08:36 | 38120 | `b557b7cb6adfef961f8755e3d1de5b2a5628e25f34c225c9e927bacb17493cce` |
| `resolucao-cmn-5274-2025-bcb-api.json` | Res. CMN nº 5.274/2025 | ficha e texto (campo Texto, HTML) | `https://www.bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Resolu%C3%A7%C3%A3o%20CMN&p2=5274` | 02/10/2026 23:08:37 | 44194 | `393b1516f3544dacdb3d133c695e3fcf1fae2ad497340183428ac92fcb0d99ee` |
| `in-rfb-1585-2015-receita-api.json` | IN RFB nº 1.585/2015 | texto em segmentos, cada um com os marcadores `tachado`, `original` e `compilado`; vigente; publicada no DOU de 02/09/2015 | `https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/67494/visao/multivigente` | 02/10/2026 23:30:14 | 522239 | `c46bb0274f3f10a606163e9ab8ca418b4a7c5be3c6e5176e58bfbe0aae39dd22` |
| `ato-declaratorio-cn-67-2025-mpv-1303.htm` | Ato Declaratório do Presidente da Mesa do Congresso Nacional nº 67/2025 | declara encerrado em 08/10/2025 o prazo de vigência da MP nº 1.303/2025 (DOU de 15/10/2025) | `https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/congresso/adc-67-mpv1.303.htm` | 02/10/2026 23:29:06 | 4595 | `f25cbd46fdfe5c02c9fffd14f5a7c3d7f69c94bedc308d6f89be7dac2222dc21` |
| `tesouro-direto-regras-e-regulamento-texto.txt` | Tesouro Direto, página "Regras e Regulamento" | **texto extraído**, não o arquivo original (ver observação) | `https://www.tesourodireto.com.br/sobre-o-tesouro/regras-e-regulamento` | 02/10/2026 23:28:59 | 25646 | `94b4a293909c3a365c9e6c56b1fbc3e89266bbded16ad545ebba0fa42beceea4` |

## Observações

- **Planalto:** cada lei e o decreto têm duas páginas. A `compilado` traz a redação vigente; a outra mantém as
  redações anteriores tachadas, o que alimenta os metadados de vigência. Codificação `windows-1252`.
- **BCB, Res. CMN nº 4.222/2013 (FGC):** o campo `Texto` da API traz só a redação original de 2013. As versões
  consolidadas são PDFs; a mais recente é a v19, que já incorpora a Res. CMN nº 5.295/2026 (alterações a partir
  de 01/06/2026). A v19 `_L` tem 39 páginas, como o PDF arquivado.
- **BCB, demais resoluções:** a resposta da API é JSON; o texto está no campo `Texto` (HTML), com as redações
  anteriores marcadas por `<s>` e as notas "Redação dada pela...". O campo `Atualizacoes` lista as normas que alteraram cada uma.
- **Res. CVM nº 30/2021 e Res. CMN nº 4.557/2017:** os PDFs arquivados já têm texto; não foram baixados de novo.
- A conferência destes textos contra os PDFs arquivados e contra os itens do D2 é o passo seguinte.
- **Corpus ampliado (decisão do autor, 02/10/2026):** entram a IN RFB nº 1.585/2015, o Regulamento e a página de
  Regras do Tesouro Direto e o Ato Declaratório CN nº 67/2025. A IN foi localizada pelo id 67494 do sistema de
  normas da Receita (o endereço antigo `normas.receita.fazenda.gov.br/sijut2consulta/link.action` redireciona por
  JavaScript para o aplicativo `normasinternet2`, que entrega o texto pela API registrada acima).
- **Tesouro Direto, página de Regras:** o site bloqueia o terminal (erro 403, proteção contra robôs) e não houve
  contorno. A página foi obtida pelo navegador. A resposta HTML original tinha 216.649 bytes e SHA-256
  `b9c5a08ffb24fc5c9d5aaa6ad25f4585afc9b4e163465e0cccbc2d4d27f00bc0`, mas não pôde ser gravada em disco. O arquivo
  arquivado é o texto dessa resposta, extraído no navegador (DOMParser; sem `script`, `style` e `noscript`;
  espaços e linhas em branco normalizados; do título "Quais são as taxas" até antes do rodapé). O SHA-256 da tabela
  foi calculado no navegador e conferido na cópia local, que inclui 47 espaços não separáveis (U+00A0).
  O texto da página contém duas imprecisões: diz "15% para aplicações com prazo acima de 721 dias" (a Lei nº
  11.033/2004 e a IN nº 1.585/2015 dizem acima de 720) e cita a "Instrução Normativa RFB nº 1.585/14" (é de 2015).
- **Regulamento do Tesouro Direto (PDF):** pendente. O site também bloqueia o terminal. Pelo navegador, o arquivo
  `REGULAMENTO_DO_TESOURO_DIRETO___11.10.2024.pdf` tinha 500.605 bytes e SHA-256
  `9a192368200466ff1c5198e6ee89d34dfe51088e6d6c69209a3f1116d21270eb` em 02/10/2026 23:28:59 UTC
  (`https://www.tesourodireto.com.br/documents/20117/0/REGULAMENTO_DO_TESOURO_DIRETO___11.10.2024.pdf/cb59ae6b-4c6a-f9ba-16c9-dd4ab44c12d5?version=1.0&t=1752002939555&download=true`).
  Deve ser baixado manualmente e conferido contra esse hash antes de entrar na pasta.
