import time
from openai import OpenAI

client = OpenAI()

def get_completion(prompt, model="gpt-4o-mini"):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

def safe_call(prompt, retries=3):
    for _ in range(retries):
        try:
            return get_completion(prompt)
        except Exception as e:
            time.sleep(2)
    return None