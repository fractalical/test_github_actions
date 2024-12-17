import uvicorn
from fastapi import FastAPI

from userapi.app.db.database import create_db_and_tables
from userapi.app.routes.users import users_router
from userapi.app.routes.healthcheck import healthcheck_router


app = FastAPI()
app.include_router(users_router, prefix='/api')
app.include_router(healthcheck_router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)