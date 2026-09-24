# -*- coding: utf-8 -*-
"""
Gerador do dataset D2 -- Perguntas normativas para validacao da base RAG.

Dissertacao: Arquitetura de IA Generativa com RAG e Calculo Deterministico
             para Democratizacao da Assessoria em Renda Fixa em Bancos Publicos
Autor da pesquisa: Kelsen de Moura Espindola (IDP)

Cada item tem pergunta, gabarito e o dispositivo de origem identificado, o que
permite calcular recall@k e precisao da recuperacao ANTES da integracao da base
ao agente. Todos os gabaritos foram extraidos dos PDFs oficiais arquivados em
bibliografia/normas/ -- nenhum de memoria.

Subconjuntos:
  D2  -- recuperacao ordinaria
  D2b -- vigencia: dispositivos revogados, alterados ou objeto de tentativa
         de alteracao que nao vingou. Testa se o mecanismo de metadados de
         vigencia prioriza a redacao vigente sobre as anteriores.

TODO (autor): revisar item a item antes do uso e confirmar a redacao das
perguntas com o orientador.
"""

import csv
from pathlib import Path

C = ["id", "subconjunto", "categoria", "norma", "dispositivo",
     "pergunta", "gabarito", "arquivo_fonte", "nivel"]

N_CVM30 = "Resolucao CVM no 30/2021"
N_FGC   = "Resolucao CMN no 4.222/2013 (Regulamento do FGC, Anexo II)"
N_IR    = "Lei no 11.033/2004"
N_IOF   = "Decreto no 6.306/2007"
N_LS    = "Lei no 15.263/2025"
N_4968  = "Resolucao CMN no 4.968/2021"
N_4879  = "Resolucao CMN no 4.879/2020"
N_4893  = "Resolucao CMN no 4.893/2021"
N_5274  = "Resolucao CMN no 5.274/2025"
N_4557  = "Resolucao CMN no 4.557/2017"

F_CVM30 = "bibliografia/normas/resolucao-cvm-30-2021-suitability.pdf"
F_FGC   = "bibliografia/normas/resolucao-cmn-4222-2013-regulamento-fgc.pdf"
F_IR    = "bibliografia/normas/lei-11033-2004-ir-compilado.pdf"
F_IOF   = "bibliografia/normas/decreto-6306-2007-iof-compilado.pdf"
F_LS    = "bibliografia/normas/lei-15263-2025-linguagem-simples.pdf"
F_4968  = "bibliografia/normas/resolucao-cmn-4968-2021-controles-internos.pdf"
F_4879  = "bibliografia/normas/resolucao-cmn-4879-2020-auditoria-interna.pdf"
F_4893  = "bibliografia/normas/resolucao-cmn-4893-2021-seguranca-cibernetica.pdf"
F_5274  = "bibliografia/normas/resolucao-cmn-5274-2025-altera-4893.pdf"
F_4557  = "bibliografia/normas/resolucao-cmn-4557-2017-gerenciamento-riscos-capital.pdf"

# (subconjunto, categoria, norma, dispositivo, pergunta, gabarito, arquivo, nivel)
ITENS = [
# ---------------------------------------------------------------- suitability
("D2","suitability",N_CVM30,"art. 2o",
 "Uma instituicao pode recomendar um produto de investimento a um cliente sem antes verificar se ele e adequado ao perfil dele?",
 "Nao. O art. 2o veda que integrantes do sistema de distribuicao e consultores de valores mobiliarios recomendem produtos, realizem operacoes ou prestem servicos sem verificar sua adequacao ao perfil do cliente.",F_CVM30,"basico"),
("D2","suitability",N_CVM30,"art. 3o, caput",
 "Quais sao as tres dimensoes que precisam ser verificadas para aferir a adequacao ao perfil do cliente?",
 "Se o produto e adequado aos objetivos de investimento (I); se a situacao financeira do cliente e compativel (II); e se o cliente tem conhecimento necessario para compreender os riscos (III).",F_CVM30,"basico"),
("D2","suitability",N_CVM30,"art. 3o, § 1o",
 "Para avaliar os objetivos de investimento do cliente, o que deve ser analisado no minimo?",
 "O periodo em que o cliente deseja manter o investimento; as preferencias declaradas quanto a assuncao de riscos; e as finalidades do investimento.",F_CVM30,"intermediario"),
("D2","suitability",N_CVM30,"art. 3o, § 2o",
 "Para avaliar a situacao financeira do cliente, o que deve ser analisado no minimo?",
 "O valor das receitas regulares declaradas; o valor e os ativos que compoem o patrimonio; e a necessidade futura de recursos declarada pelo cliente.",F_CVM30,"intermediario"),
("D2","suitability",N_CVM30,"art. 3o, § 3o",
 "Para avaliar o conhecimento do cliente sobre riscos, o que deve ser analisado no minimo?",
 "Os tipos de produtos, servicos e operacoes com que tem familiaridade; a natureza, o volume, a frequencia e o periodo das operacoes ja realizadas no mercado de valores mobiliarios; e a formacao academica e a experiencia profissional.",F_CVM30,"intermediario"),
("D2","suitability",N_CVM30,"art. 3o, § 4o",
 "A analise da formacao academica e da experiencia profissional se aplica a todo tipo de cliente?",
 "Nao. O § 4o dispensa essa analise quando o cliente for pessoa juridica.",F_CVM30,"avancado"),
("D2","suitability",N_CVM30,"art. 3o, § 5o",
 "Os custos do produto entram na verificacao de adequacao ao perfil?",
 "Sim. O § 5o exige considerar custos diretos e indiretos, abstendo-se de recomendar produtos que, isoladamente ou em conjunto, impliquem custos excessivos e inadequados ao perfil do cliente.",F_CVM30,"avancado"),
("D2","suitability",N_CVM30,"art. 4o",
 "O que a instituicao deve fazer com o cliente depois de coletar as informacoes de perfil?",
 "Avaliar e classificar o cliente em categorias de perfil de risco previamente estabelecidas.",F_CVM30,"basico"),
("D2","suitability",N_CVM30,"art. 5o, paragrafo unico",
 "Ao classificar as categorias de produtos, o que deve ser considerado no minimo?",
 "Os riscos associados ao produto e a seus ativos subjacentes; o perfil dos emissores e prestadores de servicos; a existencia de garantias; e os prazos de carencia.",F_CVM30,"intermediario"),
("D2","suitability",N_CVM30,"art. 6o",
 "Em quais situacoes e vedado recomendar produtos ou servicos ao cliente?",
 "Quando o produto ou servico nao for adequado ao perfil (I); quando nao forem obtidas as informacoes que permitam identificar o perfil (II); e quando as informacoes de perfil nao estiverem atualizadas (III).",F_CVM30,"basico"),
("D2","suitability",N_CVM30,"art. 7o",
 "Se o cliente, mesmo assim, ordenar a operacao inadequada ao seu perfil, o que a instituicao deve fazer antes da primeira operacao?",
 "Alertar o cliente sobre a ausencia, desatualizacao ou inadequacao do perfil, indicando as causas da divergencia, e obter declaracao expressa de que ele esta ciente.",F_CVM30,"intermediario"),
("D2","suitability",N_CVM30,"art. 7o, paragrafo unico",
 "Ha alguma hipotese em que o alerta e a declaracao expressa do art. 7o sao dispensados?",
 "Sim, quando o cliente estiver comprovadamente implementando recomendacoes fornecidas por consultor de valores mobiliarios autorizado pela CVM.",F_CVM30,"avancado"),
("D2","suitability",N_CVM30,"art. 8o, § 1o",
 "Em que prazo a nomeacao ou substituicao do diretor responsavel deve ser informada a CVM?",
 "Em 7 (sete) dias uteis.",F_CVM30,"avancado"),
("D2","suitability",N_CVM30,"art. 8o, § 2o",
 "Ate quando o diretor responsavel deve encaminhar o relatorio anual aos orgaos de administracao?",
 "Ate o ultimo dia util do mes de abril, relativo ao ano civil anterior a data de entrega.",F_CVM30,"avancado"),
("D2","suitability",N_CVM30,"art. 9o, I",
 "Com que periodicidade maxima as informacoes de perfil do cliente devem ser atualizadas?",
 "Observando os criterios e a periodicidade de atualizacao cadastral previstos na norma de PLDFT, respeitado o intervalo maximo de 5 (cinco) anos.",F_CVM30,"intermediario"),
("D2","suitability",N_CVM30,"art. 9o, II",
 "Com que periodicidade as categorias de valores mobiliarios devem ser reclassificadas?",
 "Em intervalos nao superiores a 24 (vinte e quatro) meses.",F_CVM30,"intermediario"),
("D2","suitability",N_CVM30,"art. 10",
 "Em quais hipoteses a verificacao de adequacao ao perfil nao e obrigatoria?",
 "Cliente investidor qualificado, salvo as pessoas naturais do art. 11, IV e do art. 12, II e III (I); cliente pessoa juridica de direito publico (II); cliente com carteira administrada discricionariamente por administrador autorizado pela CVM (III); e cliente com perfil ja definido por consultor autorizado pela CVM, implementando a recomendacao dele (IV).",F_CVM30,"avancado"),
("D2","suitability",N_CVM30,"art. 11, IV",
 "Qual o valor minimo de investimentos financeiros para que uma pessoa natural seja considerada investidor profissional?",
 "Valor superior a R$ 10.000.000,00, com atestacao por escrito mediante termo proprio, conforme o Anexo A.",F_CVM30,"intermediario"),
("D2","suitability",N_CVM30,"art. 12, II",
 "Qual o valor minimo de investimentos financeiros para que uma pessoa natural seja considerada investidor qualificado?",
 "Valor superior a R$ 1.000.000,00, com atestacao por escrito mediante termo proprio, conforme o Anexo B.",F_CVM30,"intermediario"),
("D2","suitability",N_CVM30,"art. 14",
 "Por quanto tempo os documentos e declaracoes exigidos pela norma de suitability devem ser mantidos?",
 "Pelo prazo minimo de 5 (cinco) anos contados da ultima recomendacao prestada ou da ultima operacao realizada, ou por prazo superior se a CVM determinar expressamente em processo administrativo.",F_CVM30,"intermediario"),
("D2","suitability",N_CVM30,"art. 16",
 "O descumprimento de quais dispositivos da Resolucao CVM no 30/2021 constitui infracao grave?",
 "A inobservancia das vedacoes e deveres estabelecidos nos arts. 6o e 7o, para efeito do art. 11, § 3o, da Lei no 6.385/1976.",F_CVM30,"avancado"),
("D2","suitability",N_CVM30,"art. 18",
 "Desde quando a Resolucao CVM no 30/2021 esta em vigor?",
 "Desde 1o de junho de 2021.",F_CVM30,"basico"),
# ---------------------------------------------------------------------- FGC
("D2","garantia",N_FGC,"art. 2o, § 2o",
 "Qual o valor maximo garantido pelo FGC por CPF contra o mesmo conglomerado financeiro?",
 "R$ 250.000,00 por CPF, considerado o conjunto das instituicoes do mesmo conglomerado financeiro.",F_FGC,"basico"),
("D2","garantia",N_FGC,"art. 2o, § 3o",
 "Existe algum limite de garantia do FGC alem do teto por conglomerado?",
 "Sim. Ha um teto global de R$ 1.000.000,00 por CPF a cada periodo de quatro anos consecutivos, somando as garantias pagas em todas as instituicoes associadas, independentemente do conglomerado.",F_FGC,"avancado"),
("D2","garantia",N_FGC,"art. 2o, § 4o, II",
 "Se o cliente tem aplicacoes em duas instituicoes diferentes do mesmo conglomerado, os valores sao somados para fins de garantia?",
 "Sim. Os creditos sao somados por CPF no conjunto das instituicoes do mesmo conglomerado, e o teto de R$ 250.000,00 se aplica a essa soma.",F_FGC,"intermediario"),
("D2","garantia",N_FGC,"art. 2o, § 4o, V",
 "Como a garantia do FGC e calculada em conta conjunta?",
 "O valor garantido e limitado a R$ 250.000,00 para a conta, dividido pelo numero de titulares, e o credito correspondente e atribuido individualmente a cada um deles.",F_FGC,"avancado"),
# --------------------------------------------------------------- tributacao
("D2","tributacao",N_IR,"art. 1o",
 "Quais sao as aliquotas da tabela regressiva do Imposto de Renda sobre aplicacoes de renda fixa?",
 "22,5% ate 180 dias; 20% de 181 a 360 dias; 17,5% de 361 a 720 dias; e 15% acima de 720 dias.",F_IR,"basico"),
("D2","tributacao",N_IR,"art. 1o",
 "Uma aplicacao resgatada exatamente no 360o dia fica sujeita a qual aliquota de IR?",
 "20%, porque a faixa de 181 a 360 dias inclui o 360o dia; a aliquota de 17,5% so comeca a partir do 361o dia.",F_IR,"avancado"),
("D2","tributacao",N_IOF,"art. 32 e Anexo",
 "Sobre qual base o IOF incide nas aplicacoes de renda fixa resgatadas antes de 30 dias?",
 "Sobre o rendimento, nunca sobre o principal, limitado ao percentual da tabela do Anexo conforme o numero de dias corridos.",F_IOF,"intermediario"),
("D2","tributacao",N_IOF,"art. 32 e Anexo",
 "Qual o percentual limite de IOF sobre o rendimento em um resgate feito no 15o dia?",
 "50% do rendimento.",F_IOF,"avancado"),
("D2","tributacao",N_IOF,"art. 32 e Anexo",
 "A partir de quantos dias o IOF deixa de incidir sobre o rendimento?",
 "A partir de 30 dias corridos, quando o percentual limite passa a ser zero.",F_IOF,"basico"),
# ---------------------------------------------------------- linguagem simples
("D2","linguagem",N_LS,"Lei no 15.263/2025",
 "O que a Lei no 15.263/2025 instituiu e a quem se aplica?",
 "Instituiu a Politica Nacional de Linguagem Simples, vinculante para toda a administracao publica, o que alcanca os bancos publicos.",F_LS,"basico"),
("D2","linguagem",N_LS,"Lei no 15.263/2025",
 "A Lei no 15.263/2025 fixa algum indice ou valor numerico de legibilidade a ser atingido?",
 "Nao. A lei estabelece a politica e seus principios, mas nao define valor numerico especifico de legibilidade.",F_LS,"avancado"),
# ------------------------------------------------------ governanca e controles
("D2","governanca",N_4968,"art. 3o",
 "Quais sao os tres objetivos dos sistemas de controles internos das instituicoes financeiras?",
 "Desempenho, informacao e conformidade.",F_4968,"intermediario"),
("D2","governanca",N_4879,"art. 1o a 3o",
 "A quem a unidade de auditoria interna deve estar subordinada?",
 "Diretamente ao conselho de administracao, admitida a contratacao de auditor independente nas condicoes do art. 3o, § 1o.",F_4879,"intermediario"),
("D2","governanca",N_4893,"art. 2o, § 1o",
 "A politica de seguranca cibernetica deve ser igual para todas as instituicoes?",
 "Nao. Deve ser compativel com o porte, o perfil de risco e o modelo de negocio da instituicao.",F_4893,"intermediario"),
("D2","governanca",N_4893,"art. 2o, § 2o",
 "Um conglomerado prudencial pode adotar uma unica politica de seguranca cibernetica para todas as suas instituicoes?",
 "Sim. A norma admite politica unica por conglomerado prudencial ou sistema cooperativo.",F_4893,"avancado"),
("D2","governanca",N_4557,"estrutura geral",
 "A estrutura de gerenciamento de riscos e proporcional ao porte da instituicao?",
 "Sim. A norma organiza as exigencias por segmento prudencial (S1 a S5) e exige a Declaracao de Apetite por Riscos (RAS) e programa de testes de estresse.",F_4557,"intermediario"),
("D2","governanca",N_5274,"art. 3o, § 2o, XIV",
 "O monitoramento de informacoes na Deep Web e na Dark Web e exigencia expressa da regulamentacao de seguranca cibernetica?",
 "Sim. O inciso XIV exige acoes de inteligencia no ambiente cibernetico, incluindo o monitoramento de informacoes de interesse da instituicao na internet, na Deep Web e na Dark Web, alem de grupos privados de comunicacao.",F_5274,"avancado"),
# ================================================== D2b -- vigencia
("D2b","vigencia",N_CVM30,"art. 11, VII",
 "Na redacao vigente do art. 11, VII, da Resolucao CVM no 30/2021, qual e a denominacao correta da categoria profissional listada?",
 "Assessores de investimento. A redacao anterior dizia agentes autonomos de investimento; o inciso foi alterado pela Resolucao CVM no 162/2022 e novamente pela Resolucao CVM no 179/2023, que fixou a denominacao atual.",F_CVM30,"avancado"),
("D2b","vigencia",N_CVM30,"art. 12, III",
 "Na redacao vigente do art. 12, III, a certificacao mencionada e requisito para o registro de qual categoria?",
 "Assessores de investimento, conforme redacao dada pela Resolucao CVM no 179/2023, que substituiu a mencao anterior a agentes autonomos de investimento.",F_CVM30,"avancado"),
("D2b","vigencia",N_CVM30,"art. 11, IX",
 "Fundos patrimoniais sao considerados investidores profissionais?",
 "Sim. O inciso IX foi incluido pela Resolucao CVM no 162/2022 e nao constava da redacao original de 2021.",F_CVM30,"avancado"),
("D2b","vigencia",N_CVM30,"art. 17",
 "A Instrucao CVM no 539/2013 continua em vigor?",
 "Nao. Foi expressamente revogada pelo art. 17 da Resolucao CVM no 30/2021.",F_CVM30,"intermediario"),
("D2b","vigencia",N_4893,"art. 3o, § 2o",
 "Quantos procedimentos e controles minimos de seguranca cibernetica a norma vigente exige?",
 "Quatorze, conforme a redacao do art. 3o, § 2o, dada pela Resolucao CMN no 5.274/2025.",F_4893,"avancado"),
("D2b","vigencia",N_4893,"revogacoes",
 "As Resolucoes CMN no 4.658/2018 e no 4.752/2019 continuam em vigor?",
 "Nao. Ambas foram revogadas pela Resolucao CMN no 4.893/2021.",F_4893,"intermediario"),
("D2b","vigencia",N_4879,"revogacoes",
 "A Resolucao CMN no 4.588/2017 continua em vigor?",
 "Nao. Foi revogada pela Resolucao CMN no 4.879/2020, que tambem revogou o art. 46 da Resolucao no 4.656/2018.",F_4879,"avancado"),
("D2b","vigencia",N_4968,"ambito de aplicacao",
 "Administradoras de consorcio e instituicoes de pagamento estao no ambito de aplicacao da Resolucao CMN no 4.968/2021?",
 "Nao. As exclusoes de ambito foram atualizadas pela Resolucao CMN no 5.117/2024 e alcancam administradoras de consorcio, instituicoes de pagamento, corretoras e distribuidoras de valores mobiliarios e corretoras de cambio.",F_4968,"avancado"),
("D2b","vigencia",N_5274,"art. 2o",
 "Qual foi o prazo de adequacao concedido pela Resolucao CMN no 5.274/2025?",
 "Ate 1o de marco de 2026. A norma foi publicada em 18/12/2025 e entrou em vigor na data da publicacao.",F_5274,"avancado"),
("D2b","vigencia",N_IR,"art. 1o",
 "A tabela regressiva do IR sobre renda fixa foi substituida por aliquota unica pela Medida Provisoria no 1.303/2025?",
 "Nao. A MP no 1.303/2025 propos a substituicao, mas caducou em 08/10/2025 sem conversao em lei, de modo que a tabela regressiva da Lei no 11.033/2004 permaneceu vigente sem interrupcao.",F_IR,"avancado"),
("D2b","vigencia",N_IOF,"art. 32",
 "Os decretos de 2025 sobre IOF alteraram a tabela de IOF sobre aplicacoes de renda fixa?",
 "Nao. O art. 32 e o Anexo do Decreto no 6.306/2007 nao foram alterados pelos Decretos no 12.466, 12.467 e 12.499, de 2025, que trataram de IOF sobre credito, cambio e seguro.",F_IOF,"avancado"),
("D2b","vigencia",N_4557,"redacao vigente",
 "A ementa da Resolucao CMN no 4.557/2017 esta na redacao original?",
 "Nao. A ementa tem redacao dada pela Resolucao no 4.745/2019, e o texto consolidado incorpora alteracoes ate a Resolucao CMN no 5.194/2024.",F_4557,"avancado"),
]

if __name__ == "__main__":
    destino = Path(__file__).parent / "d2-perguntas.csv"
    with destino.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(C)
        for i, it in enumerate(ITENS, 1):
            sub = it[0]
            w.writerow([f"{sub}-{i:03d}"] + list(it))
    print(f"{len(ITENS)} itens gravados em {destino.name}")
