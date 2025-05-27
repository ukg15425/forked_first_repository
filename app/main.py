import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def home():
    # changes for the second time
    
    try:
        stringa = None
        # if isinstance(stringa,str):
        #     result ='furia balcanica'
        # else:
        #     result = 7865
        if stringa:
            print('ciao')
        return result
    except Exception as e:
        
        raise Exception('You raised an conflict') from e

if __name__ == '__main__':
    uvicorn.run(
        app, 
        host='127.0.0.1', 
        port=8000, 
        reload=True
    )
