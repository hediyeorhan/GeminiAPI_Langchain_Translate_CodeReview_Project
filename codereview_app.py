from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from typing import List
from fastapi import FastAPI
import os

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key = os.getenv("GEMINI_API_KEY"))

system_template = """
Review the following {language} code and provide feedback. 
Identify potential issues, inefficiencies, or deviations from best practices. 
Suggest improvements and explain why they would enhance the code.
"""

# ciktiyi turkce olarak almak istersek 
system_template2 = "{language} programlama dilinde verilen kodu review ederek güncel kod halini ve geri bildirimlerini benimle paylaşır mısın?"


prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{code}")]
)

parser = StrOutputParser()

chain = prompt_template | model | parser

app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":    
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
    
    
    
