import json

movie = {
    "name":"ZERO",
    "director":"idk",
    "runtime":"4hrs",
    "actors":["unknown1","unknown2","forgotten3"],
    "budget":333333
}

output = open("favourite.json", "w")

json.dump(movie, output, indent = 4)

output.close()