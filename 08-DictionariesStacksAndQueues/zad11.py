import json

with open("generated.json") as file:
    data = json.load(file)

    for i in data:
        for k,v in i.items():
            print(k,":",v)