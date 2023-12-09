<h1 align="center">Добро пожаловать на страницу проекта <a href="https://proseptmatching.zapto.org/" target="_blank">Система разметки товаров</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>

Backend для проекта хакатона "Яндекс.Практикум" и "ПРОСЕПТ"

## Авторы

- [Владислав Тарасов](https://github.com/BAR2LEHI)
- [Анастасия Пушкарная](https://github.com/Anastasia7Si)

<div id="header" align="center">
  <img src="https://img.shields.io/badge/Python-3.11-F8F8FF?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/FastAPI-0.104.1-F8F8FF?style=for-the-badge&logo=FastAPI&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-555555?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0.23-F8F8FF?style=for-the-badge&logo=SQLAlchemy&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-555555?style=for-the-badge&logo=docker&logoColor=2496ED">
  <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
  <img src="https://img.shields.io/badge/Pytest-009639?style=for-the-badge&logo=pytest&logoColor=white">
</div>

## Технологии

**Client:** Python 3.11 , Fastapi 0.104, Uvicorn 0.24, SQLAlchemy 2.0, alembic 1.12, python-dotenv 1

**Server:** Docker 6.1.3, Postgres 13, Nginx 1.25

[## Ссылка на архив](https://disk.yandex.ru/d/Nn06mJ8VADMxNQ)

## Реализовано:
Бэкенд приложения написан с помощью фреймворка FastAPI и библиотек SQLAlchemy, Pydantic. Что позволяет выделить несколько преимуществ:
 - Высокая скорость работы.
 - Возможность реализации асинхронного кода.
 - Встроенная валидация данных.

Проект настроен на работу с СУБД PostgreSQL, что так же позволяет обрабатывать большие объемы трафика и масштабировать базу данных в зависимости от потребностей.
Осуществлён запуск частей проекта (Backend, Fronted, DS) через систему контейнеризации. Что облегчает работу каждого направления в отдельности и помогает при общем тестировании системы.
На сервере заказчика проект запущен в режиме “product”, на сайте настроен HTTPS, доступ осуществляется по доменному имени.

## Запуск проекта

### Для запуска проекта локально (доступ по http://127.0.0.1:8000/)

- Клонировать репозиторий и перейти в него:
```
git clone git@github.com:Anastasia7Si/project_backend.git
cd project_backend
```

- Создать файл .env в корневой директории и прописать в него свои данные.
Пример:
```
POSTGRES_PASSWORD=db_password
POSTGRES_USER=db_user
POSTGRES_DB=db_name
POSTGRES_PORT=db_port
POSTGRES_SERVER=db_host_name
```

- Выполнить загрузку данных в БД при первом запуске согласно load_db.example.py.

- Подготовить сервер PostgreSQL согласно данным в вашем .env-файле.

- Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
- Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
- Создать и применить миграции:
```
alembic revision --autogenerate -m "migration"
alembic upgrade head
```
- Запустить проект:
```
uvicorn src.main:app
```

### Для запуска контейнеров (доступ по http://localhost:80/)
- Перейти в папку infra/ и создать в нём .env файл согласно примеру:
```
cd infra/
```
- Запустить сборку  проекта:
```
docker-compose up -d
```
- При первом запуске необходимо загрузить данные в БД сделав GET-запрос на адрес удобный(добавленный) адрес, пример скрипта для загрузки находится в load_db.example.py.

### Для запуска проекта на сервере (доступ по http://(domen_name)/)

- Скопировать на сервер файл docker-compose.prod.yml и рядом с ним создать .env файл (по примеру выше) и nginx.conf с настройками по примеру nginx.conf в папке infra.

- Запустить сборку  проекта:
```
sudo docker compose -f docker-compose.prod.yml up -d
```

## Запуск тестов
- Для запуска тестов необходимо выполнить команду:
```
python tests.py
```
## К проекту подключена документация, в которой можно ознакомиться с эндпоинтами и методами, а также с примерами запросов, ответов и кода:
```
http://127.0.0.1:8000/docs/
```
