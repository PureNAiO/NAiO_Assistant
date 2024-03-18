import requests


class Actor:
    def call_robot(self, robot_url):
        url = robot_url + '/api/action'
        payload = {'ip': '10.1.1.254',
                   'issue_ip': '192.168.111.111',
                   'if_name': 'vlan 888'}
        response = requests.post(url, json=payload)

    def call_insight(self, insight_url):
        url = insight_url + '/api/warning'
        payload = {'device_name': '10.1.1.254',
                   'warn_msg': 'Interface Vl888 of GZ-CoreSW Failed'}
        response = requests.post(url, json=payload)