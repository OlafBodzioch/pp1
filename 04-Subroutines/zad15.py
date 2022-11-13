import mymath

liczba = mymath.read_number()

random = mymath.generate_number()

if liczba==random:
    print("Gratulacje! Zgadłeś/aś liczbę! ")
else:
    print(f"Źle!! Losowo wygenerowana liczba to: {random}")