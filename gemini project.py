import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("key")
client = genai.Client(api_key=api_key)

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    response = client.models.generate_content(model="gemini-3.6-flash",contents=question)
    print("Gemini:",response.text)