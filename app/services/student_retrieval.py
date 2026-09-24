from sqlalchemy.orm import Session

from ..database.database import SessionLocal
from ..database.models import Student


def get_all_students():

    db: Session = SessionLocal()

    try:
        students = db.query(Student).all()

        student_data = []

        for student in students:
            student_data.append({
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "course": student.course,
                "email": student.email
            })

        return student_data

    finally:
        db.close()

def search_student_by_name(name: str):

    db: Session = SessionLocal()

    try:
        students = db.query(Student).filter(
            Student.name.ilike(f"%{name}%")
        ).all()

        student_data = []

        for student in students:
            student_data.append({
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "course": student.course,
                "email": student.email
            })

        return student_data

    finally:
        db.close()