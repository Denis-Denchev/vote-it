import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# --- Постави root в sys.path ---
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

print("DEBUG sys.path:", sys.path)

# --- Alembic конфигурация ---
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --- IMPORT Base и модели ---
from app.api.db.base import Base
from app.api.models.user import User
import app.api.models.poll
import app.api.models.ballot
import app.api.models.audit_log


target_metadata = Base.metadata

print("DEBUG tables:", list(target_metadata.tables.keys()))

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
