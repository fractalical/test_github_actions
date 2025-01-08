import pytest

from starlette.testclient import TestClient

from app.main import app
from app.db.database import create_db_and_tables, drop_db_and_tables

test_client = TestClient(app)


@pytest.fixture(autouse=True, scope='function')
def clear_db():
    create_db_and_tables()
    yield
    drop_db_and_tables()
