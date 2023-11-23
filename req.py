import requests
from data import Data

class Request:
    def __init__(self, data):
        self.data = data
        self.TOKEN = data.getToken()
        self.API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
        self.headers = {"Authorization": f"Bearer {self.TOKEN}"}

    def get(self, request):
        request = {"inputs": request}
        r = requests.post(self.API_URL, headers=self.headers, json=request)
        print(r)
        return r.json()
    
if __name__ == "__main__":
    data = Data("private/data.priv")
    req = Request(data)
    print(req.get("Hello, my name is"))