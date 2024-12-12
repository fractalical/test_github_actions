from fastapi import FastAPI

from app.routes.users import users_router


app = FastAPI()
app.include_router(users_router)
