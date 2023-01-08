import json
import re

def f(age,course,average):
    count = 0
    file = open("test.json","r")
    data=json.load(file)

    for i in data:
        if i["age"]>=age:
            for j in i["studies"]["courses"]:
                if j["name"]==course:
                    grades = 0
                    for x in j["grades"]:
                        grades+=x
                    if grades/len(j["grades"])>=average:
                        count +=1
    return count

print(f(21, "statistics", 4))