#!/bin/sh

alembic current

alembic revision --autogenerate -m "migration"


alembic upgrade head

exec uvicorn src.main:app --proxy-headers --host 0.0.0.0 --port 8000