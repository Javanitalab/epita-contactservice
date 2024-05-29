import requests


class OutlookServiceConnector():

    def __init__(self):
        self.url = 'http://localhost:8002/'

    def send_ping(self):

        response = requests.get(url=endpoint)

        if response.status_code == 200:
            return True
        else:
            return False

    def create_contact(self, endpoint: str, data: dict):

        response = requests.post(url=endpoint, data=data)

        return response

    def get_authorization_url(self):

        response = requests.get(
            url=f'{self.url}outlook-auth/get_authorization_url/'
        )

        return response
