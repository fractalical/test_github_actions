from typing import Annotated

from fastapi import Depends
from sqlmodel import    Session, SQLModel, create_engine


db_url = f"postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"

connect_args = {"check_same_thread": False}
engine = create_engine(db_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]