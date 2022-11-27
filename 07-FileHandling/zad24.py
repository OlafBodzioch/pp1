import re

with open("vowels.txt",'r',encoding='utf-8') as file:
    for row in file:
        match = re.findall('[aeiou]', row, re.IGNORECASE)

print(f"There are {len(match)} vowels in the text")

file.close()