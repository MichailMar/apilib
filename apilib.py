import requests


class ApiMonitor:
    token = ""

    def __init__(self, token):
        self.token = token

    def request(self, method, params):
        resp = requests.get("http://91.210.168.170:3000/api/{0}/{1}?{2}".format(self.token, method, params))
        return resp.json()