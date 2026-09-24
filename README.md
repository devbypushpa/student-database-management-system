
# Student Database Management System

A backend API project for managing student information using Python and FastAPI.

## Features

- Create student records
- Retrieve student records
- Update student information
- Delete student records
- Input validation using Pydantic
- SQLite database using SQLAlchemy
- Interactive API documentation using Swagger
- Gemini AI integration
- LangGraph chatbot integration
- Student information retrieval

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Google Gemini API
- LangGraph
- Pytest

## API Documentation

After running the application, open:

http://127.0.0.1:8000/docs

## Run the Project

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

## Testing

Run automated tests:

```bash
python -m pytest -v
```

## Project Status

- CRUD operations completed
- Input validation completed
- Gemini integration completed
- LangGraph chatbot completed
- Automated tests completed