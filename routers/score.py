from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List

from crud import score as ScoreCrud
from schemas import score

router = APIRouter(prefix="/score", tags=["Scores"])

@router.get("/{score_id}", response_model=score.Score)
def get(score_id: int, db: Session = Depends(get_db)):
    score = ScoreCrud.get_score(db, score_id)
    if score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return score

@router.post("/", response_model=score.Score)
def create_score(data: score.ScoreCreate, db: Session = Depends(get_db)):
    return ScoreCrud.create_score(db=db, data=data)

@router.patch("/{score_id}", response_model=score.Score)
def update_score(score_id: int, data: score.ScoreUpdate, db: Session = Depends(get_db)):
    score = ScoreCrud.update_score(db=db, score_id=score_id, data=data)
    if score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return score

@router.delete("/{score_id}", response_model=score.Score)
def delete_score(score_id: int, db: Session = Depends(get_db)):
    score = ScoreCrud.delete_score(db=db, score_id=score_id)
    if score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return score