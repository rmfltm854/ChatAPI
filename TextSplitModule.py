from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import os
# from langchain.text_splitter import RecursiveCharacterTextSplitter
def GenerateTextSplitter():
    documents = []
    for file in os.listdir('/Users/jominsu/Desktop/Papers/'):
        if file.endswith('.pdf'):
            pdf_path = '/Users/jominsu/Desktop/Papers/' + file
            print(pdf_path)
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())
        elif file.endswith('.docx') or file.endswith('.doc'):
            doc_path = '/Users/jominsu/Desktop/Papers/' + file
            loader = Docx2txtLoader(doc_path)
            documents.extend(loader.load())
        elif file.endswith('.txt'):
            text_path = '/Users/jominsu/Desktop/Papers/' + file
            loader = TextLoader(text_path)
            documents.extend(loader.load())
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunked_documents = text_splitter.split_documents(documents)
    return chunked_documents