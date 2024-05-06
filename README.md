## Parte deste código foi adaptada do repositório plebhash/btcbrl
Link para o repositório original: https://github.com/plebhash/btcbrl

Para garantir que o `cryptocompare` esteja disponível:

```
$ python3 -m venv .
$ source bin/activate
$ pip3 install cryptocompare
```

Use o 'btcbrl.py' da seguinte forma:
```
$ python3 btcbrl.py <brl_oferta> <%_premium_vendedor>
```

## Rode com Docker

```
docker run --rm jaonoctus/btcbrl <brl_oferta> <%_premium_vendedor>
```
