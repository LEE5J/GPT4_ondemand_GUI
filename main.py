import os
from config import API_KEY
from openai import OpenAI
client = OpenAI(api_key=API_KEY)

completion = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {"role":"system","content":""},
    {"role":"user","content":"""
    """}
  ]
)

print(completion.choices[0].message.content)
