import uuid, os,json

class Data:
    def __init__(self, name_file):
        self.data = {}
        self.name_file = name_file
        
    def __str__(self):
        return str(self.data)
    
    def load_data(self):
        if not self.name_file in os.listdir("private"):
            self.save_data()
            return
        with open(f"private/{self.name_file}", 'r') as f:
            self.data = json.load(f)

    def save_data(self):
        with open(f"private/{self.name_file}", 'w') as f:
            json.dump(self.data, f, indent=4)

    def get_history(self):
        print(self.data)

        return self.data["history"]

    def getToken(self):
        with open("private/token.priv", "r") as f:
            return f.read()
        
    def clear_history(self):
        self.data["history"] = []
        self.save_data()