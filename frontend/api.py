import requests
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

origins = ["*"]

@app.get('/')
async def getHome():
    return FileResponse('../index.html')

@app.post('/read-image')
async def readImage(req: Request):
    # Front API for digit-reader
    url = 'http://digitreader-service:8081/read-image'
    content = await req.body()

    response = requests.post(url, json = content)

    return (response.text)

# Code other services here.

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8081)