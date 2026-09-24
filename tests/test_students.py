import pytest

from pydantic import ValidationError

from app.schemas.student import StudentCreate


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