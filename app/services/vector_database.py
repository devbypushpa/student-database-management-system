
import chromadb

from ..services.student_retrieval import get_all_students


# Create a persistent ChromaDB client
client = chromadb.PersistentClient(
    path="./chroma_db"
)


# Create or access the student collection
collection = client.get_or_create_collection(
    name="students"
)


def add_students_to_vector_db():

    students = get_all_students()

    if not students:
        return {
            "message": "No students found in the database"
        }

    documents = []
    ids = []
    metadatas = []

    for student in students:

        student_id = str(student["id"])

        document = (
            f"Name: {student['name']}, "
            f"Age: {student['age']}, "
            f"Course: {student['course']}, "
            f"Email: {student['email']}"
        )

        documents.append(document)
        ids.append(student_id)

        metadatas.append({
            "name": student["name"],
            "course": student["course"]
        })

    collection.upsert(
        ids=ids,
        documents=documents,
        metadatas=metadatas
    )

    return {
        "message": "Students added to vector database",
        "total_students": len(students)
    }


def search_students_in_vector_db(query: str):

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    return {
        "query": query,
        "documents": results.get("documents", []),
        "metadatas": results.get("metadatas", [])
    }