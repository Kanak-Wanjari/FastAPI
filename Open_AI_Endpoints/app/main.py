from fastapi import FastAPI
from app.routers import openai_routes

app = FastAPI()

app.include_router(openai_routes.router, prefix="/api/v1/openai/generate") # actual route = www.hireskilldev.com/api/v1

@app.get("/")
def read_root():
    return{"message": "Open AI FastAPI is up and Working"}