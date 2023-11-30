import requests
from data import Data
import threading

class Request:
    # Class to make request to the API
    def __init__(self, data): 
        self.data = data
        self.TOKEN = data.get_token()
        self.API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
        self.headers = {"Authorization": f"Bearer {self.TOKEN}"}

    def get(self, request):
        # Make a request to the API
        request = {"inputs": request}
        r = requests.post(self.API_URL, headers=self.headers, json=request)
        return r.json()