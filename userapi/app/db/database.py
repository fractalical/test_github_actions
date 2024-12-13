from typing import Annotated

from fastapi import Depends
from sqlmodel import    Session, SQLModel, create_engine


db_url = f"postgresql://postgres:postgres@test-course-postgres:5432/postgres"

engine = create_engine(db_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def drop_db_and_tables():
    SQLModel.metadata.drop_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]