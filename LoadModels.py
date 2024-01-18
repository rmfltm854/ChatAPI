import os

os.environ['OPENAI_API_KEY'] = ''
from langchain.chat_models import ChatOpenAI
import openai

def LoadGPT(question):
    llm = ChatOpenAI(temperature=0,  # 창의성 (0.0 ~ 2.0)
                     max_tokens=2048,  # 최대 토큰수
                     model_name='gpt-3.5-turbo',  # 모델명
                     )
    return llm


