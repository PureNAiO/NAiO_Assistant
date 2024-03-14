import json
from sd import Service
from actor import Actor
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
service = Service('AC4F7788-8EE5-4C9A-A58D-73453D2A7D83')
robot = Actor('http://127.0.0.1:5004/api/action')


class ZabbixData(BaseModel):
    device_name: str
    datas: dict


@app.post("/api/datas")
async def create_ticket(msg: ZabbixData):
    device_name = msg.device_name
    issue_data = msg.datas
    with open('ticket_example.json') as f:
        temp = json.load(f)
    temp["request"]["subject"] = f'{issue_data['if_name']} of {device_name} has been down!'
    ticket_body = json.dumps(temp, indent=4)
    result = service.create_ticket(ticket_body)
    if result != 'OK':
        print('error')
    # To SAGA Robot
    robot.call_robot(issue_data['if_name'])