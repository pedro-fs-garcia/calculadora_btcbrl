import sys
import cryptocompare
import requests
from flask import Flask, render_template, request
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"

app = Flask(__name__)



def get_ammount():
    try:
        brl_oferta = float(request.form["brl_oferta"].replace(",", "."))
    except ValueError:
        brl_oferta = 0
    
    try:
        premium = float(request.form["premium"].replace(",", "."))
    except ValueError:
        premium = 0

    try:
        quantidade_btc = float(request.form["quantidade_btc"].replace(",", "."))
    except ValueError:
        quantidade_btc = 0
    
    btc_brl = cryptocompare.get_price('BTC','BRL')['BTC']['BRL']
    btc_usd = cryptocompare.get_price('BTC','USD')['BTC']['USD']

    btc_brl_premium = btc_brl * ((100.0 + premium) / 100.0 )

    if quantidade_btc != 0:
        btc_vendido = quantidade_btc
        brl_oferta = quantidade_btc*btc_brl_premium
    else:
        btc_vendido = brl_oferta / btc_brl_premium
    
    sats_vendido = btc_vendido * 100_000_000

    preco_atual = f"R$ {btc_brl:.2f}"
    preco_atual_usd = f"$ {btc_usd:.2f}"
    premium_vendedor = f"{premium:.2f}%"
    preco_compra = f"R$ {btc_brl_premium:.2f}"
    oferta = f"R$ {brl_oferta:.2f}"
    
    btc_vendido = f"{btc_vendido:.8f} BTC"
    sats_vendido = f"{sats_vendido:.0f} sats"

    items = [preco_atual, preco_atual_usd, premium_vendedor, preco_compra, oferta, btc_vendido, sats_vendido]

    return render_template("index.html", items = items, valores=True)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        return get_ammount()
    return render_template("index.html", valores=False)


if __name__ == "__main__":
    app.run(debug=True)