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

    
def test_update_student():

    client = TestClient(app)

    student_data = {
        "name": "Update Test Student",
        "age": 20,
        "course": "BCA",
        "email": f"update.{uuid4()}@example.com"
    }

    create_response = client.post(
        "/students/",
        json=student_data
    )

    assert create_response.status_code == 200

    student_id = create_response.json()["id"]

    updated_data = {
        "name": "Updated Student",
        "age": 21,
        "course": "BCA",
        "email": f"updated.{uuid4()}@example.com"
    }

    update_response = client.put(
        f"/students/{student_id}",
        json=updated_data
    )

    assert update_response.status_code == 200

    data = update_response.json()

    assert data["name"] == "Updated Student"
    assert data["age"] == 21
    assert data["email"] == updated_data["email"]


def test_delete_student():

    client = TestClient(app)

    student_data = {
        "name": "Delete Test Student",
        "age": 22,
        "course": "BCA",
        "email": f"delete.{uuid4()}@example.com"
    }

    create_response = client.post(
        "/students/",
        json=student_data
    )

    assert create_response.status_code == 200

    student_id = create_response.json()["id"]

    delete_response = client.delete(
        f"/students/{student_id}"
    )

    assert delete_response.status_code == 200

    assert delete_response.json()["message"] == (
        "Student deleted successfully"
    )

    get_response = client.get(
        f"/students/{student_id}"
    )

    assert get_response.status_code == 404

    
def test_update_student_not_found():

    client = TestClient(app)

    updated_data = {
        "name": "Unknown Student",
        "age": 21,
        "course": "BCA",
        "email": f"unknown.{uuid4()}@example.com"
    }

    response = client.put(
        "/students/999999",
        json=updated_data
    )

    assert response.status_code == 404

    assert response.json()["detail"] == (
        "Student not found"
    )


def test_delete_student_not_found():

    client = TestClient(app)

    response = client.delete(
        "/students/999999"
    )

    assert response.status_code == 404

    assert response.json()["detail"] == (
        "Student not found"
    )

    
def test_vector_db_sync():

    client = TestClient(app)

    response = client.post(
        "/vector-db/sync"
    )

    assert response.status_code == 200

    data = response.json()

    assert "message" in data
    assert "total_students" in data


def test_vector_db_search():

    client = TestClient(app)

    sync_response = client.post(
        "/vector-db/sync"
    )

    assert sync_response.status_code == 200

    response = client.post(
        "/vector-db/search",
        json={
            "query": "BCA students"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["query"] == "BCA students"
    assert "documents" in data
    assert "metadatas" in data