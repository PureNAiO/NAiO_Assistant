import requests


class Actor:
    def __init__(self, robot_url):
        self.url = robot_url
        self.cache = {'Interface Gi0/22': '1.1.1.1'}

    def call_robot(self, if_name):
        payload = {'ip': '10.1.1.254',
                   'en_pass': 'luojm@4096',
                   'if_name': self.cache[if_name]}
        response = requests.post(self.url, json=payload)

