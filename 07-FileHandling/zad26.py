import re

file = open("text.txt",'r',encoding='utf-8')

for row in file:
    match = re.findall('\w+', row, re.IGNORECASE)

for x in match:
    if len(x)>6:
        print(x)
    
file.close()