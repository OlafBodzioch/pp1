file = open("randomizer.txt",'w',encoding='utf-8')


for i in range(1,11):
    for j in range(1,4):
        file.write(str((i)**(j)))
        if(j<3):
            file.write(", ")
    file.write("\n")

file.close()