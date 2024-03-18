import json
import os
from sd import Service
from actor import Actor
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
service = Service(os.environ.get('SD_URL'), os.environ.get('SD_TOKEN'))
robot = Actor()
robot_url = 'http://127.0.0.1:5003'
insight_url = 'http://127.0.0.1:5002'


class ZabbixData(BaseModel):
    device_name: str
    datas: dict


@app.post("/api/datas")
async def create_ticket(msg: ZabbixData):
    device_name = msg.device_name
    issue_data = msg.datas
    with open('ticket_example.json') as f:
        temp = json.load(f)
    temp["request"]["subject"] = f"{issue_data['if_name']} of {device_name} has been down!"
    ticket_body = json.dumps(temp, indent=4)
    result = service.create_ticket(ticket_body)
    if result != 'OK':
        print('error')
    # To SAGA Robot
    robot.call_robot(robot_url)
    robot.call_insight(insight_url)
