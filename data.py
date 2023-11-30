import os,json

class Data:
    def __init__(self, name_file):
        # Class to manage the data
        self.data = {
            "history": []
        }
        self.name_file = name_file
        
    def __str__(self):
        # Return the data in string
        return str(self.data)
    
    def load_data(self):
        # Load the data from the file
        if not self.name_file in os.listdir("private"):
            self.save_data()
            return
        with open(f"private/{self.name_file}", 'r') as f:
            # Load the data from the file
            self.data = json.load(f)

    def save_data(self):
        # Save the data in the file
        with open(f"private/{self.name_file}", 'w') as f:
            json.dump(self.data, f, indent=4)

    def get_history(self):
        # Return the history
        return self.data["history"]

    def get_token(self):
        # Return the token
        with open("private/token.priv", "r") as f:
            return f.read()
        
    def clear_history(self):
        # Clear the history
        self.data["history"] = []
        self.save_data()

    def delete_history(self, index):
        # Delete a message from the history
        self.data["history"].pop(index)
        self.save_data()

    def add_history(self, request, response):
        # Add a message in the history
        self.data["history"].append([request, response])
        self.save_data()

    def delete_history_message(self, message):
        # Delete a message from the history
        for index, history in enumerate(self.data["history"]):
            if history[0] == message:
                self.delete_history(index)
                return