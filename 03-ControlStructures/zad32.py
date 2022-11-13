import random

print(f"")

x=-6
z=1
i=0

#najgorszy sposób

while x is not 49:
    i=i+1

    x = x+7

    if x==49:
        print(f"{x}")
        break

    if i%7==0:
        if x>9:
            print(f"{x}")
            z = z + 1
            x = z - 7
            i = 0
        else:
            print(f" {x}")
            z = z + 1
            x = z - 7
            i = 0
    else:
        if x>9:
            print(f"{x}", end=" ")
        else:
            print(f" {x}", end=" ")

print(f"")

#dobry sposób

for i in range (1, 8):

    x = i

    for j in range (1, 8):
        
        if j==7:
            if x>9:
                print(f"{x}")
            else:
                print(f" {x}")
        else:
            if x>9:
                print(f"{x}", end=" ")
            else:
                print(f" {x}", end=" ")

        x = x + 7

print(f"")