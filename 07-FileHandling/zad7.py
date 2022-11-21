file = open("countries.txt",'r')

count = 1

for line in file:
    print(count, line, end="")
    count = count + 1


file.close()
