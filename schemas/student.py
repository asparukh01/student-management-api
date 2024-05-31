from pydantic import BaseModel

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    age: int
    class_name: str

    class Config:
        orm_mode = True    

#StudentCU - StudentCreateUpdate
class StudentCU(StudentBase):
    pass

class Student(StudentBase):
    student_id: int
