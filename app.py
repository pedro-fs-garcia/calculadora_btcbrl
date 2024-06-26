import cryptocompare
import requests
from flask import Flask, render_template
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"

app = Flask(__name__)


@app.route("/")
def home():
    btc_brl = cryptocompare.get_price('BTC','BRL')['BTC']['BRL']
    btc_usd = cryptocompare.get_price('BTC','USD')['BTC']['USD']
    return render_template('index.html', info = [btc_brl, btc_usd])


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)