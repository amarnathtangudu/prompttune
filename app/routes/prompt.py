# app/routes/prompt.py
from fastapi import APIRouter, HTTPException
from app.schemas.prompt import PromptSchema, PromptResponseSchema
from app.services.open_ai_service import analyze_prompt, improve_prompt

router = APIRouter()


@router.post("/analyze", response_model=PromptResponseSchema)
def analyze(prompt: PromptSchema):
    try:
        analysis = analyze_prompt(prompt.text)
        improvement = improve_prompt(prompt.text)
        return PromptResponseSchema(analysis=analysis, improvement=improvement)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
