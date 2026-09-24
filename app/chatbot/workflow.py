
from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from ..services.gemini_service import ask_gemini
from ..services.student_retrieval import (
    get_all_students,
    search_student_by_name
)


class ChatState(TypedDict):
    question: str
    answer: str


def chatbot_node(state: ChatState):

    question = state["question"]

    students = get_all_students()

    matched_students = []

    for student in students:

        student_name = student["name"].lower()

        if student_name in question.lower():

            matched_students = search_student_by_name(
                student["name"]
            )

            break

    if matched_students:

        student_context = "\n".join(
            [
                f"ID: {student['id']}, "
                f"Name: {student['name']}, "
                f"Age: {student['age']}, "
                f"Course: {student['course']}, "
                f"Email: {student['email']}"
                for student in matched_students
            ]
        )

    else:

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

Here is the student database information:

{student_context}

Answer the following question using the database information
when required.

Question: {question}

If the information is not available in the database,
clearly say that it is not available.
"""

    answer = ask_gemini(prompt)

    return {
        "question": question,
        "answer": answer
    }


def create_chatbot():

    graph = StateGraph(ChatState)

    graph.add_node("chatbot", chatbot_node)

    graph.add_edge(START, "chatbot")
    graph.add_edge("chatbot", END)

    return graph.compile()