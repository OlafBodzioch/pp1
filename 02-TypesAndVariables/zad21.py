from pickle import FALSE, TRUE
import random
random.seed()

x=random.randint(1,6)

z=int(input("Podaj numer od 1 do 6."))

if x==z:
    print("True")
else:
    print("False")