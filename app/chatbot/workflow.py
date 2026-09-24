
from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from ..services.gemini_service import ask_gemini
from ..services.student_retrieval import get_all_students
from ..services.vector_database import search_students_in_vector_db


class ChatState(TypedDict):
    question: str
    answer: str


def chatbot_node(state: ChatState):

    question = state["question"]

    # Search relevant student information
    # using ChromaDB vector search.

    try:

        vector_results = search_students_in_vector_db(
            question
        )

        documents = vector_results.get(
            "documents", []
        )

        if documents and documents[0]:

            student_context = "\n".join(
                documents[0]
            )

        else:

            student_context = ""

    except Exception:

        student_context = ""


    # Fallback to SQL database if
    # vector search does not return results.

    if not student_context:

        students = get_all_students()

        student_context = "\n".join(
            [
                f"ID: {student['id']}, "
                f"Name: {student['name']}, "
                f"Age: {student['age']}, "
                f"Course: {student['course']}, "
                f"Email: {student['email']}"
                for student in students
            ]
        )


    prompt = f"""
You are a student database assistant.

Use the following student database information
to answer the user's question.

Student database information:

{student_context}

Instructions:

1. Answer using the available database information.
2. Do not invent student details.
3. If the requested information is not available,
   clearly say that it is not available.
4. Give a simple and clear answer.

Question: {question}
"""


    answer = ask_gemini(prompt)

    return {
        "question": question,
        "answer": answer
    }


def create_chatbot():

    graph = StateGraph(ChatState)

    graph.add_node(
        "chatbot",
        chatbot_node
    )

    graph.add_edge(
        START,
        "chatbot"
    )

    graph.add_edge(
        "chatbot",
        END
    )

    return graph.compile()