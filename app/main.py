from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Chat2Task",
    description="Turn Messages Into Action.",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Chat2Task is running 🚀"}