from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app) 


def test_get_home(): 
    """"Testing the get endpoint""" 
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers['content-type']


def test_post_home():
    """Testing the post endpoint"""
    response = client.post("/")
    assert response.status_code  == 200 
    assert "application/json" in response.headers['content-type']
