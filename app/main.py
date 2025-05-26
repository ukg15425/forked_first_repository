import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    # changes for the second time
    print('ciao')
    return "furia balcanica"