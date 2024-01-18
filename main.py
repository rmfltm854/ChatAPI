from fastapi import FastAPI
import MainModule as module
import logging
app = FastAPI()

logger = logging.getLogger(__name__)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/home")
def home():
    return {"message":"home"}

@app.get("/GetVectorStore")
def LoadModel():
    result = module.ReturnVectorStore()
    if result == 1:
        return "EmbeddingModule Complete"
    else:
        return "[Error]EmbeddingModule ExceptionError"
