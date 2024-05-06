FROM python:3.9.18-alpine3.18

WORKDIR /usr/src/app

RUN pip install cryptocompare

COPY btcbrl.py .

ENTRYPOINT [ "python", "btcbrl.py" ]
