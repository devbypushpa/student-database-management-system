from fastapi import FastAPI

from .database.database import engine, Base
from .database import models
from .routers import students
from .services.gemini_service import ask_gemini
from .chatbot.workflow import create_chatbot
from .services.student_retrieval import get_all_students
from .services.vector_database import add_students_to_vector_db
from .services.vector_database import (
    add_students_to_vector_db,
    search_students_in_vector_db
)


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Student Database Management System",
    description="Backend API for managing student information",
    version="1.0.0"
)


app.include_router(students.router)


@app.get("/")
def home():
    return {
        "message": "Student Database Management System API is running"
    }



@app.get("/gemini-test")
def gemini_test():

    answer = ask_gemini(
        "Explain what a student database is in one simple sentence."
    )

    return {
        "question": "What is a student database?",
        "answer": answer
    }


@app.get("/chatbot-test")
def chatbot_test():

    chatbot = create_chatbot()

    result = chatbot.invoke({
        "question": "Explain FastAPI in simple words.",
        "answer": ""
    })

    return {
        "question": result["question"],
        "answer": result["answer"]
    }


@app.get("/students-data-test")
def students_data_test():

    students = get_all_students()

    return {
        "total_students": len(students),
        "students": students
    }


from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str

class SearchRequest(BaseModel):
    query: str


@app.post("/chatbot")
def chatbot(request: ChatRequest):

    chatbot = create_chatbot()

    result = chatbot.invoke({
        "question": request.question,
        "answer": ""
    })

    return {
        "question": request.question,
        "answer": result["answer"]
    }

@app.post("/vector-db/sync")
def sync_students_to_vector_db():

    result = add_students_to_vector_db()

    return result

@app.post("/vector-db/search")
def search_vector_database(request: SearchRequest):

    result = search_students_in_vector_db(
        request.query
    )

    return result