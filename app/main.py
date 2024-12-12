from fastapi import FastAPI

from app.db.database import create_db_and_tables
from app.routes.users import users_router


app = FastAPI()
app.include_router(users_router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
