from fastapi import FastAPI
from app.schemas import PromptRequest, LLMResponse
from app.services.llm_service import run_prompt

app = FastAPI(title="PromptLab – Prompt Engineering API")

@app.get("/")
def root():
    return {"message": "PromptLab API is running"}

@app.post("/{task}", response_model=LLMResponse)
def task_executor(task: str, request: PromptRequest):
    result = run_prompt(task, request.input_text)
    return LLMResponse(output=result)
