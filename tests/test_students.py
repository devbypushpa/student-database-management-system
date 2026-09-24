import pytest

from uuid import uuid4

from pydantic import ValidationError
from fastapi.testclient import TestClient

from app.schemas.student import StudentCreate
from app.main import app


def test_valid_student():

    student = StudentCreate(
        name="Anjali Sharma",
        age=20,
        course="BCA",
        email="anjali@example.com"
    )

    assert student.name == "Anjali Sharma"
    assert student.age == 20
    assert student.course == "BCA"


def test_invalid_age():

    with pytest.raises(ValidationError):

        StudentCreate(
            name="Anjali Sharma",
            age=-5,
            course="BCA",
            email="anjali2@example.com"
        )


def test_invalid_email():

    with pytest.raises(ValidationError):

        StudentCreate(
            name="Anjali Sharma",
            age=20,
            course="BCA",
            email="wrong-email"
        )


def test_get_students():

    client = TestClient(app)

    response = client.get("/students/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_student_not_found():

    client = TestClient(app)

    response = client.get("/students/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"


def test_create_student():

    client = TestClient(app)

    student_data = {
        "name": "Automated Student",
        "age": 22,
        "course": "BCA",
        "email": f"automated.{uuid4()}@example.com"
    }

    response = client.post(
        "/students/",
        json=student_data
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Automated Student"
    assert data["course"] == "BCA"
    assert data["email"] == student_data["email"]
    assert "id" in data


def test_duplicate_email():

    client = TestClient(app)

    student_data = {
        "name": "Duplicate Test Student",
        "age": 21,
        "course": "BCA",
        "email": f"duplicate.{uuid4()}@example.com"
    }

    first_response = client.post(
        "/students/",
        json=student_data
    )

    assert first_response.status_code == 200

    second_response = client.post(
        "/students/",
        json=student_data
    )

    assert second_response.status_code == 400

    assert second_response.json()["detail"] == (
        "Student with this email already exists"
    )