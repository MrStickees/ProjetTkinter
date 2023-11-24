import json

with open("private/data.json", "r") as f:
	data = json.load(f)
	print(data)