<h1 align="center">Добро пожаловать на страницу проекта <a href="https://proseptmatching.zapto.org/" target="_blank">Система разметки товаров</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>

Backend для проекта хакатона "Яндекс.Практикум" и "ПРОСЕПТ"

## Авторы

- [Владислав Тарасов](https://github.com/BAR2LEHI)
- [Анастасия Пушкарная](https://github.com/Anastasia7Si)

## Технологии

**Client:** Python 3.11 , Fastapi 0.104, Uvicorn 0.24, SQLAlchemy 2.0, alembic 1.12, python-dotenv 1

**Server:** Docker 6.1.3, Postgres 13, Nginx 1.25

## Реализовано:
```
Бэкенд приложения написан с помощью фреймворка FastAPI и библиотек SQLAlchemy, Pydantic. Что позволяет выделить несколько преимуществ:
 - Высокая скорость работы.
 - Возможность реализации асинхронного кода.
 - Встроенная валидация данных.
Проект настроен на работу с СУБД PostgreSQL, что так же позволяет обрабатывать большие объемы трафика и масштабировать базу данных в зависимости от потребностей.
Осуществлён запуск частей проекта (Backend, Fronted, DS) через систему контейнеризации. Что облегчает работу каждого направления в отдельности и помогает при общем тестировании системы.
На сервере заказчика проект запущен в режиме “product”, на сайте настроен HTTPS, доступ осуществляется по доменному имени.
``` 

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

- Запустить сборку  проекта:
```
docker-compose up -d
```

### Для запуска проекта на сервере (доступ по http://(domen_name):80/)

- Скопировать на сервер файл docker-compose.prod.yml и рядом с ним создать .env файл (по примеру выше).

- Запустить сборку  проекта:
```
sudo docker compose -f docker-compose.prod.yml up -d
```

## Запуск тестов
- 
```

```
## К проекту подключена документация, в которой можно ознакомиться с эндпоинтами и методами, а также с примерами запросов, ответов и кода:
```

```