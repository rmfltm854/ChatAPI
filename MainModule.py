import sys

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
import EmbeddingModule as em
import TextSplitModule as ts
yellow = "\033[0;33m"
green = "\033[0;32m"
white = "\033[0;39m"
def ReturnVectorStore():
    chunked_documents = ts.GenerateTextSplitter()
    vectorstore = em.EmbeddingUseOpenAI(chunked_documents)
    return vectorstore