import requests
import pytest

def test_create_patient():
    payload = {
  "patient_id": "897",
  "first_name": "Anna",
  "last_name": "Smith",
  "condition": "Diabetes"
}
    response = requests.post("http://localhost:8000/api/v1/patient", json=payload)
    assert response.status_code == 200

def test_get_patient():
    patient_id = "897"
    response = requests.get(f"http://localhost:8000/api/v1/patient/{patient_id}")
    assert response.status_code == 200