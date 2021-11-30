import pytest
from jose import jwt

from app import schemas
from app.config import settings


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_create_user(client):
    response = client.post(
        "/users/", json={"email": "test@email.com", "password": "password1234"}
    )
    assert response.status_code == 201
    assert response.json().get("email") == "test@email.com"


def test_login_user(test_user, client):
    response = client.post(
        "/login",
        data={"username": test_user["email"], "password": test_user["password"]},
    )
    login_res = schemas.Token(**response.json())
    payload = jwt.decode(
        login_res.access_token, settings.secret_key, algorithms=[settings.algorithm]
    )
    id = payload.get("user_id")
    assert response.status_code == 200
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"


@pytest.mark.parametrize(
    "email, password, status_code",
    # Parametrize allows use to test multiple values for a single test
    [
        ("wrongemail@gmail.com", "password123", 403),
        ("sanjeev@gmail.com", "wrongpassword", 403),
        ("wrongemail@gmail.com", "wrongpassword", 403),
        (None, "password123", 422),
        ("sanjeev@gmail.com", None, 422),
    ],
)
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})
    assert res.status_code == status_code
