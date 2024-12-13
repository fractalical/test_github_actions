from sqlmodel import Field, SQLModel


class UserCreate(SQLModel):
    name: str = Field(index=True, nullable=False)
    age: int | None = Field(nullable=False)


class User(UserCreate, table=True):
    id: int | None = Field(default=None, primary_key=True)
