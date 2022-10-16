import math;

a=int(input("podaj dlugosc boku a"))
b=int(input("podaj dlugosc boku b"))
c=int(input("podaj dlugosc boku c"))
p=(a+b+c)/2

wynik=math.sqrt(p*(p-a)*(p-b)*(p-c))

print(f"Wynik to: {wynik}")
