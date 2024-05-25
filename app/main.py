# app/main.py
from fastapi import FastAPI
from app.routes import prompt
import uvicorn

app = FastAPI(
    title="Prompt Improver API",
    description="An API to analyze and improve prompts using OpenAI.",
    version="1.0.0"
)

app.include_router(prompt.router, prefix="/prompts", tags=["prompts"])


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
