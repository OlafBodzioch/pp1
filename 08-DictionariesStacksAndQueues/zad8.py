person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

print(f'{person}\n')

print(f'{person["name"]}\n')

print(f'{person["hobby"]}\n')

person["surname"] = "Nowak"

print(f'{person["name"]} {person["surname"]}\n')

person["married"] = False

print(f'{person["married"]}\n')

person["gender"] = "male"

print(f'{person}\n')

person["hobby"].append("Dunno")

print(f'{person}\n')

person["phone"].update({"work": "313131444"})

print(f'{person["phone"]}\n')


