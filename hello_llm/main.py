import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_agent

model=ChatGoogleGenerativeAI(
    model= "gemini-3.5-flash-lite"
)

 

def main():
    path=os.getenv('WHYTESTING')
    print(path)
    load_dotenv()
    path=os.getenv('WHYTESTING')
    print(path)



if __name__ == '__main__':
    main()