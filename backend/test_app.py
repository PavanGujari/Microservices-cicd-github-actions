from app import app

def test_app_exists():
    assert app is not None

def test_app_can_start():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code < 500