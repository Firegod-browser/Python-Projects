import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai

# Initialize Gemini API (gets API key from environment variable)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use the latest fast Gemini model (check Google docs for up-to-date model names)
MODEL_NAME = "gemini-2.5-flash"

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_text(request: PromptRequest):
    try:
        model = genai.GenerativeModel(model_name=MODEL_NAME)
        response = model.generate_content(request.prompt)
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
