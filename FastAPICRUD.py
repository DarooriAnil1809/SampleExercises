from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

# instance of API
app = FastAPI()

# python dictionary
students = {
    1: {
        "name": "Kohli",
        "age": 35,
        "professsion": "Cricketer"
    },
    2: {
        "name": "Rohit",
        "age": 34,
        "professsion": "Cricketer"
    }
}

# endpoint


@app.get("/")
# Function
def index():
    return {"name": "FIRST API DATA"}

# Path Parameters


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="Student ID to View the Details")):
    return students[student_id]

# Query Parameters

# @app.get("/get-by-name")
# def get_student(*, name: Optional[str] = None, test: int):
#     for student_id in students:
#         if students[student_id]["name"] == name:
#             return students[student_id]
#     return {"Data": "NOT FOUND"}

# Combining Path and Query Parameters


@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "NOT FOUND"}


# Request BODY and POST METHOD
class Student(BaseModel):
    name: str
    age: int
    profession: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    profession: Optional[str] = None


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"ERROR": "STUDENT ID EXISTS"}
    students[student_id] = student
    return students[student_id]

# Request BODY- PUT METHOD


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"ERROR": "Student Doesn't Exist"}
    # if student.name != None:
    #     students[student_id].name = student.name
    # if student.age != None:
    #     students[student_id].age = student.age
    # if student.profession != None:
    #     students[student_id].name = student.profession

    students[student_id] = student
    return students[student_id]


# Request BODY- DELETE
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"ERROR": "STUDENT NOT EXISTS"}
    del students[student_id]
    return {"Message": "Deleted Successfully"}
