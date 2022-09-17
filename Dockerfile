FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["/bin/sh","-c", "./start.sh"]
