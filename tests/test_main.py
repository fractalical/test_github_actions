from tests.conftest import test_client


class TestMain:

    @staticmethod
    def test_create_user():
        response = test_client.post("/api/users/", json={"name": "first_user", "age": 18})
        assert response.status_code == 200
        assert response.json() == {"id": 1, "name": "first_user", "age": 18}

    @staticmethod
    def test_create_user_invalid_data():
        # Missing required field
        response = test_client.post("/api/users/", json={"name": "first_user"})
        assert response.status_code == 422

        # Invalid age type
        response = test_client.post("/api/users/", json={"name": "first_user", "age": "invalid"})
        assert response.status_code == 422

    @staticmethod
    def test_read_users():
        # Create test users
        test_client.post("/api/users/", json={"name": "user1", "age": 18})
        test_client.post("/api/users/", json={"name": "user2", "age": 25})

        # Test default pagination
        response = test_client.get("/api/users/")
        assert response.status_code == 200
        assert len(response.json()) == 2
        assert response.json()[0]["name"] == "user1"
        assert response.json()[1]["name"] == "user2"

        # Test pagination with limit
        response = test_client.get("/api/users/?limit=1")
        assert response.status_code == 200
        assert len(response.json()) == 1

        # Test pagination with offset
        response = test_client.get("/api/users/?offset=1")
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["name"] == "user2"

    @staticmethod
    def test_read_user():
        # Create a test user
        create_response = test_client.post("/api/users/", json={"name": "test_user", "age": 30})
        user_id = create_response.json()["id"]

        # Test getting existing user
        response = test_client.get(f"/api/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["name"] == "test_user"
        assert response.json()["age"] == 30

        # Test getting non-existent user
        response = test_client.get("/api/users/999")
        assert response.status_code == 404
        assert response.json()["detail"] == "User not found"

    @staticmethod
    def test_delete_user():
        # Create a test user
        create_response = test_client.post("/api/users/", json={"name": "to_delete", "age": 25})
        user_id = create_response.json()["id"]

        # Test deleting existing user
        response = test_client.delete(f"/api/users/{user_id}")
        assert response.status_code == 200
        assert response.json() == {"ok": True}

        # Verify user is deleted
        response = test_client.get(f"/api/users/{user_id}")
        assert response.status_code == 404

        # Test deleting non-existent user
        response = test_client.delete("/api/users/999")
        assert response.status_code == 404
        assert response.json()["detail"] == "User not found"

    @staticmethod
    def test_healthcheck():
        response = test_client.get("/healthcheck")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    @staticmethod
    def test_healthcheck_db_failure(mocker):
        # Mock database failure
        mocker.patch("sqlmodel.Session.exec", side_effect=Exception("DB Error"))
        
        response = test_client.get("/healthcheck")
        assert response.status_code == 503
        assert response.json()["detail"] == "Service Unavailable"
