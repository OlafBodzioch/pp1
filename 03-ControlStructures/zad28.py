x = 0
y = 1

print(f"{x} ")

for i in range(0,48):
    z = x
    x = x + y
    y = z
    print (f"{x}")