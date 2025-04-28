from fastapi import FastAPI
from app.routers import items
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router)

@app.get("/")
def read_root():
    return{"message": "FastAPI is up and Working"}

@app.get("/api/v1/openai/generate/feedback")
def openai_generate_feedback():
    return{"message": "this api is for generating feedback"}