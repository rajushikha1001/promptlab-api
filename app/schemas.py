from pydantic import BaseModel

class PromptRequest(BaseModel):
    input_text: str

class LLMResponse(BaseModel):
    output: str
