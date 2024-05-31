from models import Student
from sqlalchemy.orm import Session
from schemas import student

def create_student(data: student.StudentCU, db: Session):
    student = Student(
        first_name = data.first_name, 
        last_name = data.last_name, 
        age = data.age,
        class_name = data.class_name
        )
    
    try: 
        db.add(student)
        db.commit()
        db.refresh(student)
    except Exception as e:
        print(e)

    return student

def get_student(student_id: int, db: Session):
    return db.query(Student).filter(Student.student_id==student_id).first()

def update_student(data: student.StudentCU, db: Session, student_id: int):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    student.first_name = data.first_name
    student.last_name = data.last_name
    student.age = data.age
    student.class_name = data.class_name
    db.add(student)
    db.commit()
    db.refresh(student)

    return student

def delete_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.student_id==student_id).first()
    if student:
        db.delete(student)
        db.commit()
    return student