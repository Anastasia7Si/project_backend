# project_backend
Backend для проекта хакатона "Яндекс.Практикум" и "ПРОСЕПТ"

## Авторы:
```
- Владислав Тарасов(https://github.com/BAR2LEHI)
- Анастасия Пушкарная(https://github.com/Anastasia7Si)
```

## Технологии:
```
- Python 3.
- Fastapi 0.104
- Uvicorn 0.24
- SQLAlchemy 2.0
- Gunicorn 21.2
- Docker 6.1.3
```

## Реализовано: 
```
``` 

## В работе: 
```
```

## Запуск
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Anastasia7Si/project_backend.git
cd project_backend
```

### Переход в папку с docker-compose для запуска контейнеров (доступ по http://localhost/api/v1/)
```
cd infra/
```
- Создать файл .env и прописать в него свои данные.
Пример:
```
```
Запуск проекта
```
docker-compose up -d
```
Создание суперпользователя
```
docker-compose exec backend python manage.py createsuperuser
```

### Переход в папку с backend для запуска проекта локально (доступ по http://127.0.0.1:8000/)
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Запустить проект:
```

```

## Запуск тестов
- 
```

```
## К проекту подключена документация, в которой можно ознакомиться с эндпоинтами и методами, а также с примерами запросов, ответов и кода:
```

```