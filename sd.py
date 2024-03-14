import requests


class Service:
    def __init__(self, service_token):
        self.url = "https://servicedesk.f1.hk/api/v3/"
        self.headers = {"authtoken": service_token,
                        "Content-Type" : "application/x-www-form-urlencoded"}

    def get_requests(self, filter_id):
        url = self.url + "requests"
        input_data = {
            "list_info": {
                "row_count": 300,
                "filter_by": {
                    "id": filter_id
                }
            }
        }

        params = {'input_data': str(input_data)}
        response = requests.get(url, headers=self.headers, params=params, verify=False)
        if response.ok:
            return response.json()['requests']

    def get_request(self, t_id):
        url = self.url + "requests/" + t_id
        response = requests.get(url, headers=self.headers, verify=False)
        if response.ok:
            return response.json()

    def create_ticket(self, ticket_body):
        url = self.url + "requests"
        payload = {'input_data': ticket_body}
        response = requests.post(url, headers=self.headers, data=payload, verify=False)
        if response.ok:
            return 'OK'
        else:
            return response.text
