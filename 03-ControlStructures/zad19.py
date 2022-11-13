wiek = int(input("Podaj wiek w ludzkich latach. "))

if wiek <= 2:
    wiekpsa = 10.5*wiek
else:
    wiekpsa = 10.5 * 2 + (wiek-2)*4

print(f"Wiek ludzki: {wiek}")
print(f"Wiek psi: {wiekpsa}")