import requests


class Actor:
    def __init__(self, robot_url):
        self.url = robot_url

    def call_robot(self):
        payload = {'ip': '10.1.1.254',
                   'issue_ip': '192.168.111.111',
                   'if_name': 'vlan 888'}
        response = requests.post(self.url, json=payload)

