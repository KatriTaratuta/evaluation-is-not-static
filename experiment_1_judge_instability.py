import pandas as pd
import numpy as np
from utils import safe_call
from config import JUDGE_PROMPT, N_RUNS

ANSWER = "Photosynthesis is the process by which plants convert sunlight into energy."

def evaluate():
    scores = []

    for _ in range(N_RUNS):
        prompt = f"{JUDGE_PROMPT}\n\nAnswer:\n{ANSWER}"
        result = safe_call(prompt)

        try:
            score = float(result)
            scores.append(score)
        except:
            continue

    return scores

if __name__ == "__main__":
    scores = evaluate()

    print("Scores:", scores)
    print("Mean:", np.mean(scores))
    print("Std:", np.std(scores))

    df = pd.DataFrame(scores, columns=["score"])
    df.to_csv("results/judge_instability.csv", index=False)