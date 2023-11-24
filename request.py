import requests
from data import Data
import threading

class Request:
    def __init__(self, data):
        self.data = data
        self.TOKEN = data.get_token()
        self.API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
        self.headers = {"Authorization": f"Bearer {self.TOKEN}"}

    def get(self, request):
        request = {"inputs": request}
        r = requests.post(self.API_URL, headers=self.headers, json=request)
        return r.json()