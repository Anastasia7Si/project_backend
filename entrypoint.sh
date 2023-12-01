#!/bin/sh

alembic revision --autogenerate -m "migration"

alembic upgrade HEAD

exec uvicorn db_sql.main:app --host 0.0.0.0:8000