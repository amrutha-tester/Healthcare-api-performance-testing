import time
import random
from fastapi import FastAPI, HTTPException, Response
from prometheus_fastapi_instrumentator import Instrumentator
from pydantic import BaseModel

app = FastAPI(title="Healthcare EHR Service")

# Expose metric endpoint at /metrics
Instrumentator().instrument(app).expose(app)

# In-memory patient database
patients_db = {}

class PatientSchema(BaseModel):
    patient_id: str
    first_name: str
    last_name: str
    condition: str

@app.post("/api/v1/patient")
async def create_patient(patient: PatientSchema):
    # Simulate realistic processing delay
    time.sleep(random.uniform(0.01, 0.05)) 
    patients_db[patient.patient_id] = patient.model_dump()
    return {"status": "created", "patient_id": patient.patient_id}

@app.get("/api/v1/patient/{patient_id}")
async def get_patient(patient_id: str):
    if patient_id not in patients_db:
        raise HTTPException(status_code=404, detail="Patient Record Not Found")
    return patients_db[patient_id]