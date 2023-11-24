import uuid, os,json

class Data:
    def __init__(self, name_file):
        self.data = {}
        self.name_file = name_file
        
    def __str__(self):
        return str(self.data)
    
    def load_data(self):
        if not self.name_file in os.listdir():
            self.save_data()
            return
        with open(self.name, 'r') as f:
            self.data = json.load(f)

    def save_data(self):
        with open(self.name_file, "w") as f:
            json.dump(self.data, f, indent=4)

    def get_history(self):
        return self.data["history"]

    def getToken(self):
        with open("private/token.priv", "r") as f:
            return f.read()