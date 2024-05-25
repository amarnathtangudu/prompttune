# app/services/openai_service.py
import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = "sk-proj-Etj5Jsys5NabmE8SFpoIT3BlbkFJGfokqMv8AuedUExWSCqU"


def analyze_prompt(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that analyzes and improves prompts."},
            {"role": "user", "content": f"Analyze this prompt and provide feedback: {prompt}"}
        ]
    )
    return response.choices[0].message['content'].strip()


def improve_prompt(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that improves user prompts."},
            {"role": "user", "content": f"Here is a user prompt: {prompt}\nProvide an improved version of this prompt."}
        ]
    )
    return response.choices[0].message['content'].strip()
