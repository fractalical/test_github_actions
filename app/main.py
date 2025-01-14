from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from app.monitoring import http_requests_total
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

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


@app.get("/metrics")
async def metrics():
    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )


@app.middleware("http")
async def monitor_requests(request, call_next):
    response = await call_next(request)
    http_requests_total.labels(
        method=request.method,
        endpoint=request.url.path,
        status=response.status_code
    ).inc()
    return response
