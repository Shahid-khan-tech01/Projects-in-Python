from google import genai
from google.genai.types import GenerateContentResponse

client = genai.Client(api_key="AQ.Ab8RN6Jt7-uoRDTFNaWRFdm85n8_ZHe405Ko0duhsThLHErvjA")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    response: GenerateContentResponse = client.models.generate_content(model="gemini-3.6-flash",contents=question)
    print("Gemini:",response.text)