from application import Application
import os, json

if __name__ == "__main__":
    if not "private" in os.listdir():
        os.mkdir("private")
    if not "data.json" in os.listdir("private"):
        with open("private/data.json", "w") as f:
            json.dump({"history": []}, f, indent=4)
    if not "token.priv" in os.listdir("private"):
        with open("private/token.priv", "w") as f:
            f.write(input("Qu'elle est votre token ?\n"))
    
    app = Application("data.json")
    app.main()