import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def home():
    # changes for the second time
    print('ciao')
    return "furia balcanica"


if __name__ == '__main__':
    uvicorn.run(
        app, 
        host='127.0.0.1', 
        port=8000, 
        reload=True
    )
    