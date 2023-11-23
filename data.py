import uuid, os,json

class Data:
    def __init__(self, name_file):
        self.data = {}
        self.name_file = name_file
        self.load()
        
    def __str__(self):
        return str(self.data)
    
    def load(self):
        if not os.path.exists(self.name_file):
            self.save()
            return
        with open(self.name_file, "r") as f:
            self.data = json.load(f)

    def save(self):
        with open(self.name_file, "w") as f:
            json.dump(self.data, f, indent=4)

    def addHistory(self, message):
        self.data["history"].append(message)
        self.save()

    def getToken(self):
        with open("private/token.priv", "r") as f:
            return f.read()