
from utils import get_content_from_url, create_prompt
import typing
from langchain_openai import OpenAI

from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os
import json
from flask import Flask, request


load_dotenv() 

app = Flask(__name__)

llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))
model = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))



@app.route('/')
def regulate_content():
    data = request.json
    regulatory_urls = data.get('regulatory_urls', [])
    input_url = data.get('input_url', '')
    policy = data.get('policy', '')

    regulations_set = get_content_from_url(regulatory_urls)
    input_sets = get_content_from_url(input_url)
    
    if policy == "Finance" or len(regulatory_urls) == 0 or input_url == '':
        template = create_prompt("Financial Authority", regulations_set, input_sets[0])

    else:
        return 'Either policy not supported or provided urls are not correct...', 400

    response = llm.invoke(template) 
    return {'response': response, 'regulations_set': regulations_set, "input_sets": input_sets }, 200




if __name__ == '__main__':
   app.run()