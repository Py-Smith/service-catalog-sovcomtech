# Укажите необходимую версию python
FROM python:3.10

# Выберите папку, в которой будут размещаться файлы проекта внутри контейнера 
WORKDIR /opt/app

# Заведите необходимые переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

# Установите зависимости
RUN  apt-get update && apt-get upgrade -y \
     && pip install --upgrade pip \
     && pip install -r requirements.txt \
     && apt-get install gettext -y

# Скопируйте всё оставшееся. Для ускорения сборки образа эту команду стоит разместить ближе к концу файла. 
COPY . .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]