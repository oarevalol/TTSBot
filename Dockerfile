FROM python:3.7-alpine

RUN apk add --no-cache gcc libffi-dev musl-dev openssl-dev

COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt && rm -rf /tmp/requirements.txt

RUN mkdir /bot
COPY bot/ bot/

WORKDIR bot
CMD python bot.py
