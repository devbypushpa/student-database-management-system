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