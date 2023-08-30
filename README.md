# service-catalog-sovcomtech
Service Catalof from Sovcombank Technologies

# Перед запуском

Файл **.env_example** переиминовать в **.env**. При необходимости указать свои параметры.

# Запуск и остановка сервисов

Для запуска сервисов перейдите в корневой каталог и запустите:

```docker-compose up -d --build```

Для установки нужно выполнить:

```docker-compose down```

# Список сервисов

* catalog_api - API сервис для получения информации об услугах;
* admin_panel - Django Admin Site для внесения данных по услугам;
* kibana - сервис для просмотра индексов в ES;
* postgres13 - база данных для создания сервисов;
* elasticsearch - сервис для поиска данных по услугам;
* redis-prod - кеширование данных;

# Список доступных адресов

## Документация по API

[Swagger](http://localhost:8011/api/openapi)

## AdminPanel

[AdminPanel](http://localhost:8082/admin/)

Для доступа по умолчанию используются следующие данные:

* **admin** - user
* **admin** - password

## Kibana

[Kibana](http://localhost:5601)