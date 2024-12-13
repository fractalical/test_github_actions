from tests.conftest import test_client


class TestMain:

    @staticmethod
    def test_create_user():
        response = test_client.post("/users/", json={"name": "first_user", "age": 18})
        assert response.status_code == 200
        assert response.json() == {"id": 1, "name": "first_user", "age": 18}

    @staticmethod
    def test_read_users():
        response = test_client.post("/users/", json={"name": "first_user", "age": 18})
        assert response.status_code == 200

        response = test_client.get("/users/")
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["name"] == "first_user"
