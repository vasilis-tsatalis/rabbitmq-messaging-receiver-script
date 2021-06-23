from typing import Optional
from fastapi import FastAPI
import requests
import json

app = FastAPI()

@app.get("/")
@app.get("/queues/{queue_name}")
def read_queue_messages(queue_name: str):

    url = 'http://13.81.39.210:15672/api/queues/dcs/' + queue_name + '/get'

    myobj = '{"count":100,"requeue":"true","encoding":"auto","truncate":50000}'

    x = requests.post(url, data = myobj, auth = ('pms02', 'asdf12#$'))
    d = json.loads(x.text)
    messages = []
    for item in d:
        #print(item['payload'])
        messages.append(item['payload'])

    return {"response_status": x.status_code, "messages": messages}
