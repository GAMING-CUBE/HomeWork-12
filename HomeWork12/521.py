students_data = {
    "MrBeast": 6,
    "Ronaldo": 5,
    "Messi": 5,
    "Alex": 11,
    "Barbara": 9,
    "Sasha": 4,
    "Danya": 2,
    "Masha": 5
}

number = 0
amount = 0

for key, value in students_data.items():
    number += value
    amount += 1
    if value > number / amount:
        print(key)

