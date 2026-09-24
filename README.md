# Student Database Management System

A modular backend application for managing student information
using FastAPI, SQLAlchemy, Gemini API, and LangGraph.

## Project Overview

This project provides APIs for managing student records
and includes an AI-powered chatbot that can retrieve
information from the student database.

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Google Gemini API
- LangGraph
- Pytest


## Features

- Create a new student record
- View all students
- View a student by ID
- Update student information
- Delete a student record
- Validate student input
- AI chatbot using Gemini API
- LangGraph-based chatbot workflow
- Automated testing using Pytest
- Interactive API documentation using Swagger

## Project Structure

```text
app/
├── database/
├── schemas/
├── routers/
├── services/
└── chatbot/

tests/
└── test_students.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/students/` | Create a student |
| GET | `/students/` | Get all students |
| GET | `/students/{student_id}` | Get student by ID |
| PUT | `/students/{student_id}` | Update student |
| DELETE | `/students/{student_id}` | Delete student |
| POST | `/chatbot` | Ask the AI chatbot |

## How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd STUDENT-DATABASE
```

### 3. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy pydantic-settings python-dotenv email-validator google-genai langgraph pytest
```

### 5. Configure environment variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Never upload your actual API key to GitHub.

### 6. Run the server

```bash
uvicorn app.main:app --reload
```

### 7. Open Swagger documentation

```text
http://127.0.0.1:8000/docs
```

### 8. Run tests

```bash
python -m pytest -v
```

## Future Improvements

- Add user authentication
- Add role-based access control
- Improve chatbot question handling
- Add more automated tests
- Explore vector database integration
- Deploy the application to a suitable hosting platform