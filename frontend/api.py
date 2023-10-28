import io
import json
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, StreamingResponse
import requests
import uvicorn


app = FastAPI()

@app.get('/')
async def index(req: Request):
    return FileResponse('index.html')

@app.post('/read')
async def readImage(req: Request):
    #api : http://digitreader-service:8081/read-image
    content = await req.body()
    
    url = 'http://digitreader-service:8081/read-image'
    #url = 'http://127.0.0.1:8081/read-image'

    # string_data = content.decode('utf-8')
    # return string_data
    #jsonData=  json.loads(string_data)


    try:
        # Send a POST request with the data
        response = requests.post(url, data=content)  # You can also use data=data for form data

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and work with the response data, if any
            response_data = response.json()
            return response_data
            print(response_data)
        else:
           return print(f'HTTP Error: {response.status_code}')
    except requests.exceptions.RequestException as e:
       return print(f'Error: {e}')


@app.post('/translate')
async def translate(req: Request):
    content = await req.body()
    #api : http://translation-service:8082/translate-text
    url = 'http://translation-service:8082/translate-text'
    #url = 'http://127.0.0.1:8082/translate-text'

    string_data = content.decode('utf-8')
    #return string_data
    jsonData=  json.loads(string_data)


    try:
        # Send a POST request with the data
        response = requests.post(url, json=jsonData)  # You can also use data=data for form data

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and work with the response data, if any
            response_data = response.json()
            return response_data
            print(response_data)
        else:
           return print(f'HTTP Error: {response.status_code}')
    except requests.exceptions.RequestException as e:
       return print(f'Error: {e}')

     
@app.post('/textToSpeech')
async def convertTextToSpeech(req: Request):
    #api :http://textToSpeech-service:8083/text-to-speech
    print("get data from frontend")
    content = await req.body()
    print(content)
    url = 'http://textToSpeech-service:8083/text-to-speech'
    #url = 'http://127.0.0.1:8083/text-to-speech'

    #string_data = content.decode('utf-8')
    #return string_data
    #jsonData=  json.loads(string_data)


    try:
        # Send a POST request with the data
        response = requests.post(url, data=content,headers={'Content-Type': 'audio/mpeg'})  # You can also use data=data for form data

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and work with the response data, if any
            print(response)
            print("text-data")
            response_data = response.content
            return StreamingResponse(io.BytesIO(response_data), media_type="audio/mpeg")
            print(response_data)
            #return FileResponse(response_data, media_type="audio/mpeg")
            #return response_data
        else:
           return print(f'HTTP Error: {response.status_code}')
    except requests.exceptions.RequestException as e:
       return print(f'Error: {e}')



    return

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=7080)