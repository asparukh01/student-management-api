from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False, index=True)
    last_name = Column(String, nullable=True, index=True) 
    age = Column(Integer, nullable=False, index=True)
    class_name = Column(String(5), nullable=False, unique=True, index=True)
    score = relationship("Score", back_populates="student")


class Score(Base):
    __tablename__ = 'scores'

    score_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    subject = Column(String, index=True)
    score = Column(Integer)
    student = relationship("Student", back_populates="score")
