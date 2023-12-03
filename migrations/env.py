from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

import os
import sys


sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))



from src.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from src.database import Base
from src.dealers.models import ProductDealerKey, Dealer, DealerPrice
from src.company.models import Product

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

section = config.config_ini_section
config.set_section_option(section, 'DB_HOST', DB_HOST)
config.set_section_option(section, 'DB_NAME', DB_NAME)
config.set_section_option(section, 'DB_PASS', DB_PASS)
config.set_section_option(section, 'DB_PORT', DB_PORT)
config.set_section_option(section, 'DB_USER', DB_USER)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
