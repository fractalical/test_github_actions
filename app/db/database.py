from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

from app.config import settings


if settings.DATABASE == "postgresql":
    db_url = (
        f"postgresql://"
        f"{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@"
        f"{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/"
        f"{settings.POSTGRES_DB}"
    )
else:
    sqlite_file_name = "database.db"
    db_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(db_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def drop_db_and_tables():
    SQLModel.metadata.drop_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]