import re

count = 0
sum = 0

file = open("grades.txt",'r+',encoding='utf-8')

for row in file:
    match = re.findall('\d+\.+\d', row, re.IGNORECASE)

for x in match:
    sum = sum + float(x)
    count = count + 1
    
print(f"Srednia to: {sum/count}")

file.close()