import json

def store(name, data):
    with open(name, 'w') as json_file:
        json_file.write(json.dumps(data))

def load(name):
    with open(name) as json_file:
        data = json.load(json_file)
        return data
