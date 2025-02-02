FROM hub.hamdocker.ir/python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r development.txt

COPY ./core /app/