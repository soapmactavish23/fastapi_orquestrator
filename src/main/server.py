from fastapi import FastAPI

from src.main.routes import generate_router

app = FastAPI()

app.include_router(generate_router)