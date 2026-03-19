import pandas as pd
from utils import safe_call
from config import JUDGE_PROMPT

PROMPT = "Explain photosynthesis in simple terms."

def run():
    answers = []
    scores = []

    for _ in range(10):
        answer = safe_call(PROMPT)
        judge_input = f"{JUDGE_PROMPT}\n\nAnswer:\n{answer}"
        score = safe_call(judge_input)

        answers.append(answer)
        scores.append(score)

    return answers, scores

if __name__ == "__main__":
    answers, scores = run()

    df = pd.DataFrame({
        "answer": answers,
        "score": scores
    })

    df.to_csv("results/eval_drift.csv", index=False)