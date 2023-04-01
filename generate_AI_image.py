import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


#Generate keywords
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="",
  temperature=0.5,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.8,
  presence_penalty=0.0
)

print(response)
