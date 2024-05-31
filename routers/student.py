from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from crud import student as StudentCrud
from schemas import student

router = APIRouter(prefix="/student", tags=["Students"])

@router.post("/", response_model=student.Student)
def create(data: student.StudentCU = None, db: Session = Depends(get_db)):
    return StudentCrud.create_student(data=data, db=db)

@router.get("/{student_id}/", response_model=student.Student)
def get(student_id: int, db: Session = Depends(get_db)):
    student = StudentCrud.get_student(student_id=student_id, db=db)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.patch("/{student_id}/", response_model=student.Student)
def update(student_id: int, data: student.StudentCU, db: Session = Depends(get_db)):
    db_student = StudentCrud.get_student(db=db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return StudentCrud.update_student(student_id=student_id, data=data, db=db)

@router.delete("/{student_id}/", response_model=student.Student)
def delete(student_id: int, db: Session = Depends(get_db)):
    db_student = StudentCrud.get_student(db=db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return StudentCrud.delete_student(student_id=student_id, db=db)
