import json
import numpy as np
import os

os.makedirs("results", exist_ok=True)

# --- Experiment 1: Judge Instability ---
with open("data/judge_instability.json") as f:
    scores = json.load(f)

print("=== Judge Instability ===")
print("Scores:", scores)
print("Mean:", np.mean(scores))
print("Std:", np.std(scores))


# --- Experiment 2: Prompt Leakage ---
with open("data/prompt_leakage.json") as f:
    data = json.load(f)

print("\n=== Prompt Leakage ===")
print("\nBase example:")
print(data["base"][0])

print("\nHinted example:")
print(data["hinted"][0])

print("\nObservation:")
print("Hinted answers are more structured and formatted.")


# --- Experiment 3: Evaluation Drift ---
with open("data/eval_drift.json") as f:
    drift = json.load(f)

scores = [x["score"] for x in drift]

print("\n=== Evaluation Drift ===")
print("Scores:", scores)
print("Mean:", np.mean(scores))
print("Std:", np.std(scores))


# --- Save summary ---
with open("results/summary.txt", "w") as f:
    f.write("Judge Instability:\n")
    f.write(f"Mean: {np.mean(scores)}\nStd: {np.std(scores)}\n")