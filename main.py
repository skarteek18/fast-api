from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from datetime import datetime
import time

app = FastAPI(title="Hospital Management API")

# ---------------- DATABASE (Simple In-Memory) ----------------

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "doctor": {"password": "doctor123", "role": "doctor"}
}

doctors = []
patients = []
appointments = []

# ---------------- AUTHENTICATION ----------------

class Login(BaseModel):
    username: str
    password: str

class Doctor(BaseModel):
    name: str
    email: str
    active: bool = True

class Patient(BaseModel):
    name: str
    age: int
    doctor_id: int

class Appointment(BaseModel):
    doctor_id: int
    patient_id: int
    appointment_date: datetime
    status: str = "scheduled"


def current_user(username: str):
    if username not in users:
        raise HTTPException(401, "Invalid user")
    return users[username]


# ---------------- LEVEL 11 ----------------

@app.post("/login")
def login(data: Login):
    user = users.get(data.username)

    if not user or user["password"] != data.password:
        raise HTTPException(401, "Invalid username or password")

    return {
        "username": data.username,
        "role": user["role"],
        "token": f"token-{data.username}"
    }


@app.get("/patients")
def get_patients(username: str):
    user = current_user(username)

    if user["role"] == "doctor":
        return [p for p in patients if p["doctor_id"] == 1]

    return patients


# ---------------- LEVEL 12 ----------------

@app.post("/doctors")
def add_doctor(data: Doctor, username: str):
    if current_user(username)["role"] != "admin":
        raise HTTPException(403, "Admin access required")

    doctor = data.model_dump()
    doctor["id"] = len(doctors) + 1
    doctors.append(doctor)

    return doctor


@app.post("/patients")
def add_patient(data: Patient, username: str):
    user = current_user(username)

    if user["role"] not in ["admin", "doctor"]:
        raise HTTPException(403, "Access denied")

    patient = data.model_dump()
    patient["id"] = len(patients) + 1
    patients.append(patient)

    return patient


@app.post("/appointments")
def add_appointment(data: Appointment, username: str):
    user = current_user(username)

    if user["role"] == "doctor" and data.doctor_id != 1:
        raise HTTPException(403, "Access denied")

    if data.status not in ["scheduled", "completed", "cancelled"]:
        raise HTTPException(400, "Invalid status")

    for a in appointments:
        if (
            a["doctor_id"] == data.doctor_id
            and a["appointment_date"] == data.appointment_date
        ):
            raise HTTPException(409, "Appointment already exists")

    appointment = data.model_dump()
    appointment["id"] = len(appointments) + 1
    appointment["created_at"] = datetime.now()

    appointments.append(appointment)

    return appointment


@app.get("/appointments")
def get_appointments(username: str):
    start = time.time()

    result = appointments

    if current_user(username)["role"] == "doctor":
        result = [a for a in appointments if a["doctor_id"] == 1]

    return {
        "response_time": round(time.time() - start, 4),
        "data": result
    }


# ---------------- LEVEL 13–15 ----------------

@app.get("/doctors/{doctor_id}/appointments")
def doctor_appointments(doctor_id: int):
    return [
        a for a in appointments
        if a["doctor_id"] == doctor_id
    ]


@app.get("/patients/{patient_id}/appointments")
def patient_appointments(patient_id: int):
    return [
        a for a in appointments
        if a["patient_id"] == patient_id
    ]


# ---------------- LEVEL 16 ----------------

@app.get("/")
def home():
    return {
        "message": "Hospital API running",
        "docs": "/docs"
    }


# ---------------- LEVEL 18 ----------------

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "time": datetime.now()
    }
