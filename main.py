import uvicorn
from fastapi import FastAPI
from database import SessionLocal, engine, Base
from routers.student import router as StudentRouter
from routers.score import router as ScoreRouter

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(StudentRouter)
app.include_router(ScoreRouter)


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)