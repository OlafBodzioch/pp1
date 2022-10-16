wzrost=float(input("Podaj wzrost w metrach: "))
waga=int(input("Podaj masę ciała w kg: "))

bmi=waga/wzrost**2

print(f"Twoje bmi wynosi : {bmi}")

if bmi>18.5 and bmi<25: 
    print("BMI jest prawidłowe.")
else:
    print("BMI nie jest prawidłowe")
