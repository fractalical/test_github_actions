from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.monitoring import (
    http_requests_total,
    set_health_status,
    health_check_total
)
from app.db.database import SessionDep

healthcheck_router = APIRouter()

@healthcheck_router.get("/healthcheck")
def healthcheck(session: SessionDep):
    """
    Healthcheck endpoint to verify application and database status.
    """
    try:
        result = session.exec(select(1)).first()
        if result != 1:
            raise Exception("Database check failed")
            
        set_health_status(1)
        health_check_total.inc()
        http_requests_total.labels(method='GET', endpoint='/healthcheck', status='200').inc()
        
        return {"status": "ok"}
    except Exception as e:
        set_health_status(0)
        raise HTTPException(status_code=503, detail="Service Unavailable")
