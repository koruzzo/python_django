FROM python:3.12.1

ENV PYTHONBUFFERED 1

RUN mkdir /app-root

WORKDIR /app-root

ADD . /app-root

RUN pip install -r requirements.txt
