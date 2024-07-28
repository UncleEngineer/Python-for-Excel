# pip install openai
# pip install python-decouple
# ถ้าเพลอ pip install decouple ต้อง pip uninstall decouple ก่อน

from openai import OpenAI
from decouple import config

api_key = config("OPENAI_API_KEY")
# ใน folder เดียวกันต้องมี file .env OPENAI_API_KEY = "sk-proj-xxxxx-xxxx-xxx-xxx"

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    # {"role": "user", "content": "Where was it played?"}
  ],
  max_tokens=200
)
message = response.choices[0].message.content
print(message)
