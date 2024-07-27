from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
    id: int
    name: str
    grade: int

students = [
    Student(id=1, name="ali", grade=5),
    Student(id=3, name="muhammed", grade=6)
]

@app.get("/students/")
def read_students():
    return students

@app.post("/students/")
def create_student(new_student: Student):
    students.append(new_student)
    return new_student

@app.put("/students/{student_id}")
def update_student(student_id: int, update_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = update_student
            return update_student
    return {"error": "Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message": "Student is deleted"}
    return {"error": "Student not found"}
