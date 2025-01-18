from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

openai_api_key = os.getenv("OPENAI_API_KEY")
print(f"OpenAI API Key: {openai_api_key}")



from langchain_openai import ChatOpenAI

llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {"role": "user", "content": "introduce yourself"}
]

completion = llm.invoke(messages)
print(completion)