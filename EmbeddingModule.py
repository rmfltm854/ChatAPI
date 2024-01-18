import os

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
os.environ['OPENAI_API_KEY'] = ""

def EmbeddingUseOpenAI(chunked_documents):
    try:
        Chroma.from_documents(documents=chunked_documents, embedding=OpenAIEmbeddings(),
                              persist_directory="/Users/jominsu/Desktop/EmbeddingDirectory")
        EmbeddingStatus = 1
    except :
        EmbeddingStatus = 0

    return EmbeddingStatus