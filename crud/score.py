from sqlalchemy.orm import Session
from models import Score
from schemas.score import ScoreCreate, ScoreUpdate

def get_score(db: Session, score_id: int):
    return db.query(Score).filter(Score.score_id == score_id).first()

def create_score(db: Session, data: ScoreCreate):
    score = Score(
        student_id=data.student_id,
        subject=data.subject,
        score=data.score,
    )
    db.add(score)
    db.commit()
    db.refresh(score)
    return score

def update_score(db: Session, score_id: int, data: ScoreUpdate):
    score = db.query(Score).filter(Score.score_id == score_id).first()
    if score:
        score.subject = data.subject
        score.score = data.score
        db.commit()
        db.refresh(score)
    return score

def delete_score(db: Session, score_id: int):
    score = db.query(Score).filter(Score.score_id == score_id).first()
    if score:
        db.delete(score)
        db.commit()
    return score
