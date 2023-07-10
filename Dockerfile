FROM python:3.11.4-alpine3.18 as builder

WORKDIR /app

COPY requirements.txt .

RUN apk update \
	&& apk add --virtual build-deps gcc python3-dev musl-dev libffi-dev openssl-dev

RUN pip install --upgrade pip
RUN python -m venv /opt/venv
RUN . /opt/venv/bin/activate && pip install --no-cache-dir -r requirements.txt
RUN apk del build-deps

COPY . .

ENV FLASK_RUN_PORT=5000

EXPOSE ${FLASK_RUN_PORT}

CMD . /opt/venv/bin/activate && exec gunicorn -b :${FLASK_RUN_PORT} --access-logfile - --error-logfile - run:app
