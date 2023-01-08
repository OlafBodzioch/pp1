
x = 10
z = ""

if x>0:
    for i in range(1, x+1):
        z+="/"
        if i%5==0 and i is not x:
            z+="-"

print(z)