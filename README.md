
# Student Database Management System

A modular backend application for managing student records through REST APIs, database operations, AI-powered assistance, and vector search.

## Project Overview

The Student Database Management System is developed using Python and FastAPI. It provides APIs for managing student information and includes Gemini AI, LangGraph, and ChromaDB integration.

## Features

- Create student records
- Retrieve all students
- Retrieve a student by ID
- Update student information
- Delete student records
- Input validation using Pydantic
- Duplicate email validation
- SQLite database integration
- FastAPI Swagger/OpenAPI documentation
- Gemini API integration
- LangGraph chatbot workflow
- Student database retrieval
- ChromaDB vector database integration
- Automated testing using Pytest

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| SQLAlchemy | Database operations |
| SQLite | Student data storage |
| Pydantic | Data validation |
| Google Gemini API | AI responses |
| LangGraph | Chatbot workflow |
| ChromaDB | Vector database |
| Pytest | Automated testing |
| Git & GitHub | Version control |

## Project Structure

```text
STUDENT-DATABASE/
│
├── app/
│   ├── database/
│   │   ├── database.py
│   │   └── models.py
│   │
│   ├── schemas/
│   │   └── student.py
│   │
│   ├── routers/
│   │   └── students.py
│   │
│   ├── services/
│   │   ├── gemini_service.py
│   │   ├── student_retrieval.py
│   │   └── vector_database.py
│   │
│   ├── chatbot/
│   │   └── workflow.py
│   │
│   └── main.py
│
├── tests/
│   └── test_students.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/devbypushpa/student-database-management-system.git
```

### 2. Open the project folder

```bash
cd student-database-management-system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment on Windows

```powershell
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never share your API key or commit the `.env` file to GitHub.

## Run the Application

```bash
uvicorn app.main:app --reload
```

## API Documentation

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

FastAPI provides interactive Swagger documentation for testing the APIs.

## Main API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/students/` | Create a student |
| GET | `/students/` | Get all students |
| GET | `/students/{student_id}` | Get student by ID |
| PUT | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |
| GET | `/students-data-test` | Retrieve student data |
| POST | `/chatbot` | Ask the AI chatbot |
| GET | `/gemini-test` | Test Gemini integration |
| GET | `/chatbot-test` | Test LangGraph chatbot |
| POST | `/vector-db/sync` | Sync students to ChromaDB |
| POST | `/vector-db/search` | Search the vector database |

## Testing

Run the automated tests using:

```bash
python -m pytest -v
```

The project includes tests for:

- Student validation
- Invalid age
- Invalid email
- Retrieving students
- Student not found
- Creating a student
- Duplicate email validation

## Future Improvements

- Authentication and authorization
- Role-based access control
- Improved chatbot query routing
- Frontend interface
- Advanced student search and filtering
- Production deployment

## Author

**Pushpa Topno**

GitHub: [devbypushpa](https://github.com/devbypushpa)