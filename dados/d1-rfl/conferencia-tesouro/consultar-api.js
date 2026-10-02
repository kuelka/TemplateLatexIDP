// Reexecuta a consulta a calculadora avancada do Tesouro Direto para os casos
// de api-requisicoes.json. Uso: abrir
// https://www.tesourodireto.com.br/simuladores/calculadora-avancada, abrir o
// console do navegador, colar este arquivo, depois colar o conteudo de
// api-requisicoes.json como argumento de consultar(...). O resultado sai no
// mesmo formato de api-resultados.json:
// [id, dias corridos, dias uteis, bruto, custodia, aliquota IR %, IR, liquido,
//  codigo de status, data/hora da resposta]
async function consultar(casos) {
  const saida = [];
  for (const { id, b } of casos) {
    const r = await fetch("/o/calculadora-avancada", {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify(b),
    });
    const j = await r.json();
    saida.push([id, j.qtyDaysPurchsSale, j.qtyBizDaysPurchsSale, j.grssAmtRed,
      j.amtCtdyFeeRed, j.incmTaxAlqt, j.incmTaxAmt, j.netRedAmt,
      j.BizSts && j.BizSts.cd, j.BizSts && j.BizSts.dtTm]);
    await new Promise((ok) => setTimeout(ok, 350)); // uma consulta por vez
  }
  return JSON.stringify(saida);
}
