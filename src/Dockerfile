FROM python:3.8-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apk add libpq gcc musl-dev gettext
RUN set -e; \
    apk add --virtual .compile-deps postgresql-dev python3-dev libc-dev linux-headers; \
    pip3 install psycopg2==2.9.3 --no-cache-dir; \
    apk del --no-cache .compile-deps;

COPY . /app
RUN pip3 install pipenv==2022.1.8 psycopg2>=2.8 --no-cache-dir
RUN pipenv install --system --deploy