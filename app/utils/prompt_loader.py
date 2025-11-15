from app.config import PROMPT_DIR

def load_prompt(task: str):
    file_path = f"{PROMPT_DIR}/{task}.txt"
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
