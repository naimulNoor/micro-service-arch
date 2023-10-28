from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import uvicorn
import boto3
import random
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 
# AKIAX3X6M7S6KYAJOOG5
# A7sQMPwZj/jnW9dhzflL26RbYh4XUG8TDQ+c75gd
# us-east-1

aws_region=""
aws_access_key_id=""
aws_secret_access_key=""


def transLateTask(data):
    #convert json 
    string_data = data.decode('utf-8')
    #return string_data
    jsonData=  json.loads(string_data)
    

    
    # Initialize a Boto3 Polly client with credentials and region
    translate = boto3.client('translate', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    # Request speech synthesis
    response = translate.translate_text(
        Text=jsonData["data"],
        SourceLanguageCode="en",  # Source language code (e.g., 'en' for English)
        TargetLanguageCode=jsonData["lang"]
    )
    translated_text = response['TranslatedText']
    
    return translated_text






@app.post('/translate-text')
async def textToSpeech(req: Request):
    # save uploaded file
    content = await req.body()
    return transLateTask(content)

   

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8082)