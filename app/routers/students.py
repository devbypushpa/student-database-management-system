from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database.database import get_db
from ..database.models import Student
from ..schemas.student import StudentCreate, StudentResponse


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post("/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):

    existing_student = db.query(Student).filter(
        Student.email == student.email
    ).first()

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="Student with this email already exists"
        )

    new_student = Student(
        name=student.name,
        age=student.age,
        course=student.course,
        email=student.email
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


@router.get("/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):

    students = db.query(Student).all()

    return students


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student_data: StudentCreate,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = student_data.name
    student.age = student_data.age
    student.course = student_data.course
    student.email = student_data.email

    db.commit()
    db.refresh(student)

    return student


@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }