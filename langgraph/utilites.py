from dotenv import load_dotenv
import os
load_dotenv
from langchain.chat_models import init_chat_model, BaseChatModel

def get_default_model() -> BaseChatModel:
    """
    this method returns the default model from google
    ai studio free tier
    """
    model_name='google_genai:gemini-3.5-flash-lite'
    model=init_chat_model(model=model_name)
    return model
