from fastapi import APIRouter, HTTPException
from sqlmodel import select

from userapi.app.db.database import SessionDep

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
    except Exception as e:
        raise HTTPException(status_code=503, detail="Service Unavailable")

    return {"status": "ok"}
