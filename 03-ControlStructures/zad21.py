university = "Uniwersytet Ekonomiczny w Krakowie"

length = len(university)
i = 0

while i < length:
    print(f"{university[i]}", end = ' ')
    i=i+1

print("")
print('--------------------------------------------------------------------')

for z in range(0,length):
    print(f"{university[z]}", end = ' ')