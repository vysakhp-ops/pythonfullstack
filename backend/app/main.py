from fastapi import FastAPI
from .database import engine
from . import models
from .routers import item_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend API is running"}

app.include_router(item_router)
