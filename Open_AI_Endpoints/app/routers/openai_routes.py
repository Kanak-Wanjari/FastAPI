from fastapi import APIRouter, Body
from app.service.openai_service import *

router = APIRouter()

@router.post("/feedback")
def post_feedback(payload:dict = Body("Posting Feedback")):
    return generate_feedback(payload)

@router.post("/questions")
def post_questions(payload: dict = Body("Posting Questions")):
    return generate_questions(payload)

@router.get("/response")
def get_response():
    return generate_response()