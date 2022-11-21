import random

file = open(".\\07-FileHandling\\randomizer.txt",'w',encoding='utf-8')


for i in range(50):
    rand = str(random.randint(100,1000))
    file.write(rand+"\n")

file.close()
