file = open(".\\07-FileHandling\\numbers.txt",'r')

sum = 0

for line in file:
    sum = sum + int(line)

print(sum)

file.close()
