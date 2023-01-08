class Student():
    count = 100000

    uczelnia = "UEK"

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.album = Student.count
        Student.count+=1

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.album} ({self.uczelnia})"

x1 = Student("Bolaf", "Odzioch")
x2 = Student("Boolaf", "Dzioch")
x3 = Student("Louis", "Cypher")

print(x1)
print(x2)
print(x3)