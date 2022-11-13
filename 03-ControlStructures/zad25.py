x = 15
y = 20

for i in range(0, y):
    if i == 0 or i == y-1:
        for i in range(0, x):
            print("*", end = "")
        print("")
    else:
        for i in range(0, x):
            if i==0 or i==x-1:
                print("*", end = "")
            else:
                print(" ", end="")
        print("")
print("")