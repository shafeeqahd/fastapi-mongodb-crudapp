from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity
from bson import ObjectId

student_router = APIRouter()

@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(connection.local.student.find())

@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())

@student_router.get('/student/{studentId}')
async def find_student_by_id(studentId):
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

@student_router.put('/students/{studentId}')
async def update_student(studentId, student:Student):
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(studentId)},
        {"$set": dict(student)}
    )
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

@student_router.delete('/students/{studentId')
async def delete_student(studentId):
    return studentEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))
