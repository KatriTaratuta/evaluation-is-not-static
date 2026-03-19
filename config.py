MODEL = "gpt-4o-mini"  # might be replaced

N_RUNS = 10

JUDGE_PROMPT = """
You are an evaluator. Rate the answer from 1 to 10 based on quality, clarity, and correctness.
Return only a number.
"""