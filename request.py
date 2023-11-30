import requests

# Class to manage the request and use the inference API
class Request:
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