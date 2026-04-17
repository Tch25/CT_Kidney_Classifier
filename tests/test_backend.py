import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from main import app

client = TestClient(app)

def test_health_endpoint():
    """Test that health endpoint returns correct status"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_predict_endpoint_no_file():
    """Test predict endpoint with no file (should fail)"""
    response = client.post("/predict")
    assert response.status_code == 422  # Unprocessable entity

def test_predict_endpoint_invalid_file():
    """Test predict endpoint with invalid file type"""
    files = {"file": ("test.txt", b"not an image", "text/plain")}
    response = client.post("/predict", files=files)
    assert response.status_code == 400
    assert "File must be an image" in response.text
