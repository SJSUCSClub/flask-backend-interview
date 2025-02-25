# Welcome to ACM@SJSU Dev Team Flask Backend Interview

This technical interview will test your understanding of Flask, HTTP, and Python.

The goal of this interview is for you to develop functional routes that handle basic HTTP requests.

## Project Requirements

You are developing a professor rating backend application for SJSU, similar to Rate My Professor. This application accepts requests from the client to create, get, update, and delete reviews of professors.
Your task is to develop API routes for the `/reviews` endpoint.

Review object:
```
class Review(TypedDict):
    id: int
    professorName: str
    courseName: str
    rating: int
    grade: str
    tags: list[str]
    takeAgain: bool
    content: str
```

You must create the following routes:
- **GET** `/reviews` - Return a list of all reviews
  - Response Body: `{ reviews: list[Review] }`
  - Response Status: 200
- **POST** `/reviews` - Create a review object
  - Request Body: `Omit<Review, "id">`
  - Response Body: `{ review: Review }`
  - Response Status: 201
  > **_NOTE:_**  You can generate the `Review["id"]` however you like
- **GET** `/reviews/<id>` - Return `Review` with given id
  - Response Body: `{ review: Review }`
  - Response Status: 200
- **PUT** `/reviews/<id>` - Update `Review` with given id
  - Request Body: `Omit<Review, "id">`
  - Response Body: Not Content
  - Response Status: 204
- **DELETE** `/reviews/<id>` - Delete `Review` with given id
  - Response Body: Not Content
  - Response Status: 204

We will assume that all the requests have valid request bodies and parameters. To store the `Review` object we will use an in-memory list of `Review`, which is already provided.

## Testing
We will test using the following commands in sequence:

```
curl http://127.0.0.1:5000/reviews

curl -XPOST -H 'Content-Type: application/json' -d '{"professorName": "David Taylor", "courseName": "DSA", "rating": 3, "tags": ["java"], "takeAgain": true, "grade": "B-", "content": "hard course" }'  http://127.0.0.1:5000/reviews

curl http://127.0.0.1:5000/reviews/<id>

curl -XPUT -H 'Content-Type: application/json' -d '{"professorName": "David Taylor", "courseName": "DSA", "rating": 3, "tags": ["java"], "takeAgain": true, "grade": "A-", "content": "easy course" }'  http://127.0.0.1:5000/reviews/<id>

curl http://127.0.0.1:5000/reviews/<id>

curl -XDELETE http://127.0.0.1:5000/reviews/<id>

curl http://127.0.0.1:5000/reviews
```

windows friendly curl commands
```
curl http://127.0.0.1:5000/reviews

curl -XPOST -H "Content-Type: application/json" -d "{\"professorName\": \"David Taylor\", \"courseName\": \"DSA\", \"rating\": 3, \"tags\": [\"java\"], \"takeAgain\": true, \"grade\": \"B-\", \"content\": \"hard course\" }" http://127.0.0.1:5000/reviews

curl http://127.0.0.1:5000/reviews/<id>

curl -XPUT -H "Content-Type: application/json" -d "{\"professorName\": \"David Taylor\", \"courseName\": \"DSA\", \"rating\": 3, \"tags\": [\"java\"], \"takeAgain\": true, \"grade\": \"A-\", \"content\": \"easy course\" }" http://127.0.0.1:5000/reviews/<id>

curl http://127.0.0.1:5000/reviews/<id>

curl -XDELETE http://127.0.0.1:5000/reviews/<id>

curl http://127.0.0.1:5000/reviews
```
