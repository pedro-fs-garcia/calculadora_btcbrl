function calcular(){
    const info = [parseFloat(document.getElementById("btc/brl").innerHTML), parseFloat(document.getElementById("btc/usd").innerHTML)];
    let premium = document.getElementById("premium").value.trim();
    let brl_oferta = document.getElementById("brl_oferta").value.trim();
    let quantidade_btc = document.getElementById("qtd_btc").value.trim();
    
    if (premium === "" || isNaN(premium)) {
        premium = 0;
    } else {
        premium = parseInt(premium, 10);
    }

    let preco_final = info[0] + info[0]*premium/100;

    if(brl_oferta === "" || isNaN(brl_oferta)){
        brl_oferta = 1.00;
    }else{
        brl_oferta = parseFloat(brl_oferta, 10);
    }

    if (quantidade_btc !== "" && !isNaN(quantidade_btc)){
        quantidade_btc = parseFloat(quantidade_btc)
        brl_oferta = quantidade_btc*preco_final;
    }else{
        quantidade_btc = brl_oferta/preco_final;
    }

    let preco_compra = brl_oferta;
    let btc_vendido = brl_oferta/preco_final;
    let sats_vendido = btc_vendido*100000000;

    document.getElementById("premium_vendedor").innerHTML = premium;
    document.getElementById("preco_final").innerHTML = preco_final.toFixed(2);
    document.getElementById("preco_compra").innerHTML = brl_oferta.toFixed(2);
    document.getElementById("btc_vendido").innerHTML = btc_vendido.toFixed(8);
    document.getElementById("sats_vendido").innerHTML = sats_vendido.toFixed(0);
}