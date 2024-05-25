# app/models/prompt.py
from pydantic import BaseModel


class Prompt(BaseModel):
    text: str
