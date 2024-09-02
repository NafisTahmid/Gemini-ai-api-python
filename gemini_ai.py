from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to load Gemini Pro model and get response
model = genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream = True)
    return response

text = input("Please enter your question: ")
response = get_gemini_response(text)

for chunk in response:
    print(chunk.text)