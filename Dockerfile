FROM python:3.8

WORKDIR /var/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV PORT=8080

CMD ["./docker-entrypoint.sh"]
