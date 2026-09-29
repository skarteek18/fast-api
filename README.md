FastAPI Backend Application

Overview

This project is a FastAPI backend application for managing Doctors, Patients, and Appointments.

The project includes authentication, role-based authorization, database relationships, validation, exception handling, auditing, testing, and Swagger documentation.

Tech Stack

- Python 3.9+
- FastAPI
- SQLAlchemy
- Pydantic
- JWT
- SQLite
- Pytest
- Uvicorn

Features

Level 11 – Role-Based Authorization

Roles:

- Admin
- Doctor

Admin

- Full access to Doctor and Patient APIs
- Can manage appointments

Doctor

- Can view only assigned patients
- Cannot delete doctors
- Cannot delete patients

Unauthorized requests return "403 Forbidden".

Level 12 – Appointment Management

Appointment fields:

- "id"
- "doctor_id"
- "patient_id"
- "appointment_date"
- "status"

Appointment statuses:

- "scheduled"
- "completed"
- "cancelled"

Validation:

- Doctor must exist
- Patient must exist
- Doctor must be active
- Overlapping appointments for the same doctor are prevented

APIs:

POST   /appointments
GET    /appointments
GET    /appointments/{id}
PUT    /appointments/{id}
DELETE /appointments/{id}

GET    /doctors/{doctor_id}/appointments
GET    /patients/{patient_id}/appointments

Level 13 – Data Integrity

- Unique constraint on Doctor email
- Foreign key constraints
- Database exceptions handled gracefully
- Meaningful error messages returned to users

Example:

{
  "success": false,
  "message": "Doctor with this email already exists"
}

Level 14 – Performance

- Optimized SQLAlchemy queries
- Avoided N+1 query problems
- Added database indexes
- List API response time measurement

Level 15 – Audit & Tracking

Added:

created_at
updated_at
created_by
updated_by

The "created_by" and "updated_by" values are obtained from the authenticated JWT user.

Level 16 – API Hardening

Implemented:

- Global exception handling
- Custom error responses
- Uniform validation error responses
- Basic rate limiting

Example:

{
  "success": false,
  "message": "Patient not found",
  "error_code": "PATIENT_NOT_FOUND"
}

Level 17 – Testing

Implemented tests for:

- Authentication
- Authorization
- Doctor APIs
- Patient APIs
- Appointment APIs
- Services
- Validation

Run tests:

pytest

Run coverage:

pytest --cov=app --cov-report=term-missing

Target coverage:

70%+

Level 18 – Documentation

Swagger documentation is available at:

/docs

ReDoc:

/redoc

Documentation includes:

- API descriptions
- Request schemas
- Response schemas
- Authentication
- Status codes
- Request/response examples

Project Structure

fastapi-project/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── dependencies.py
│   ├── exceptions.py
│   │
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   └── services/
│
├── tests/
│   ├── test_auth.py
│   ├── test_doctors.py
│   ├── test_patients.py
│   ├── test_appointments.py
│   └── test_services.py
│
├── requirements.txt
├── .gitignore
└── README.md

Installation

Clone the repository:

git clone <your-github-repository-url>
cd fastapi-project

Create virtual environment:

python -m venv venv

Activate the environment.

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run Application

uvicorn app.main:app --reload

Application URL:

http://127.0.0.1:8000

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

Testing

Run all tests:

pytest

Run coverage:

pytest --cov=app --cov-report=term-missing

.gitignore

The following files are excluded from Git:

__pycache__/
*.py[cod]
venv/
.venv/
.env
*.db
*.sqlite
.pytest_cache/
.coverage
htmlcov/
.vscode/
.idea/
*.log
.DS_Store

Submission

The repository contains:

- FastAPI source code
- Authentication and authorization
- Doctor and Patient APIs
- Appointment APIs
- Database constraints
- Exception handling
- Audit tracking
- Tests
- README
- requirements.txt
- .gitignore
- Swagger/Postman screenshots
