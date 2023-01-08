import re

def f(first_letter,last_letter):
    file=open("test.txt","r", encoding="utf-8")
    
    count = 0
    
    for line in file:
        for word in line.split():
            word = re.findall("\w", word)
            if len(word)>0:
                if word[0]==first_letter and word[len(word)-1]==last_letter:
                    count = count + 1
    
    return count