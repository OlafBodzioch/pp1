x=1
sum=0
ilosc=-1

while x is not 0:
    x=int(input("Podaj x "))
    sum = sum + x
    ilosc = ilosc + 1

srednia = sum/ilosc

print(f"WYNIK: ILOSC: {ilosc} SUMA: {sum} SREDNIA: {srednia}")