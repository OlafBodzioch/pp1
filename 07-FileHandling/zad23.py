import re

count = 0
sum = 0

with open("temperatura.txt",'r',encoding='utf-8') as file:
    for line in file:
        match = re.findall('\d+', line)
        
for x in match:
    count = count+1
    sum = sum + int(x)
        
print(f'Srednia to: {sum/count}')

file.close()