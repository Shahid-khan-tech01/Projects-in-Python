from google import genai
from google.genai.types import GenerateContentResponse

client = genai.Client(api_key="API key")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    response: GenerateContentResponse = client.models.generate_content(model="gemini-3.6-flash",contents=question)
    print("Gemini:",response.text)
