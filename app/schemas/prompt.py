# app/schemas/prompt.py
from pydantic import BaseModel


class PromptSchema(BaseModel):
    text: str


class PromptResponseSchema(BaseModel):
    analysis: str
    improvement: str
