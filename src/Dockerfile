FROM python:3.10-slim

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN  pip install --upgrade pip \
     && pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /opt/app

COPY entrypoint.sh entrypoint.sh
RUN ["chmod", "+x", "/opt/app/entrypoint.sh"]
ENTRYPOINT ["/opt/app/entrypoint.sh"]