import pandas as pd
from utils import safe_call

BASE_PROMPT = "Explain what is photosynthesis."
HINT_PROMPT = "Explain what is photosynthesis. Your answer will be evaluated for clarity and structure."

def run(prompt):
    return safe_call(prompt)

if __name__ == "__main__":
    base_outputs = [run(BASE_PROMPT) for _ in range(5)]
    hint_outputs = [run(HINT_PROMPT) for _ in range(5)]

    df = pd.DataFrame({
        "base": base_outputs,
        "hinted": hint_outputs
    })

    df.to_csv("results/prompt_leakage.csv", index=False)