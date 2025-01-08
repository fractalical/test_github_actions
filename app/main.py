from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.db.database import create_db_and_tables
from app.routes.users import users_router
from app.routes.healthcheck import healthcheck_router


app = FastAPI()
app.include_router(users_router, prefix='/api')
app.include_router(healthcheck_router)


@app.get("/")
def root():
    return RedirectResponse(url="/docs")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
