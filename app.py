from flask import Flask
from typing import TypedDict

app = Flask(__name__)


class Review(TypedDict):
    id: int
    professorName: str
    courseName: str
    rating: int
    grade: str
    tags: list[str]
    takeAgain: bool
    content: str


reviews: list[Review] = [
    {
        "id": 1,
        "professorName": "John Doe",
        "courseName": "Python",
        "rating": 5,
        "grade": "A",
        "tags": ["python", "programming"],
        "takeAgain": True,
        "content": "This is a great course!",
    },
    {
        "id": 2,
        "professorName": "Jane Smith",
        "courseName": "JavaScript",
        "rating": 2,
        "grade": "B",
        "tags": ["javascript", "frontend"],
        "takeAgain": False,
        "content": "This is a bad course!",
    },
]


# write your routes here


if __name__ == "__main__":
    app.run(debug=True)
