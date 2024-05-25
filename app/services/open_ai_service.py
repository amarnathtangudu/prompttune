# app/services/openai_service.py
import os
from dotenv import load_dotenv
import openai
import base64

load_dotenv()

base64_encoded_string = "c2stcHJvai1FdGo1SnN5czVOYWJtRThTRnBvSVQzQmxia0ZKR2Zva3FNdjhBdWVkVUV4V1NDcVU="
# Decode from Base64
decoded_bytes = base64.b64decode(base64_encoded_string)

# Decode UTF-8 bytes to a string
decoded_string = decoded_bytes.decode('utf-8')
openai.api_key = decoded_string


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
