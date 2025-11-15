import openai
from app.config import OPENAI_API_KEY, MODEL_NAME
from app.utils.prompt_loader import load_prompt

openai.api_key = OPENAI_API_KEY

def run_prompt(task: str, user_input: str):
    prompt_template = load_prompt(task)
    final_prompt = prompt_template.replace("{{input}}", user_input)

    response = openai.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": final_prompt}],
        max_tokens=200
    )

    return response.choices[0].message["content"]
