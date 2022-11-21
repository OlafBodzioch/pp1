x = "countries.txt"

count = 0

filename = '.\\07-FileHandling\\'
print(filename)
filename = filename+x
print(filename)

with open(filename, 'r') as f:
    for line in f:
        print(line, end="")
    f.close()

#bbbb dozrobiena