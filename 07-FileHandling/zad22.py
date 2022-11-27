import csv
import re

with open("students.txt",'r',encoding='utf-8') as file:
    for row in file:
        match = re.findall('\d{2}', row)
        

        
        

