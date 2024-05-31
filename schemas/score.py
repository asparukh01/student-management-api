from pydantic import BaseModel

class ScoreBase(BaseModel):
    subject: str
    score: int

class ScoreCreate(ScoreBase):
    student_id: int

class ScoreUpdate(ScoreBase):
    pass

class Score(ScoreBase):
    score_id: int
    student_id: int

    class Config:
        orm_mode = True