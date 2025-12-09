import json

with open("file1") as f:
    data = json.load(f)

print(data)
print(type(data))
print(data['users'][2]['skills'][2])