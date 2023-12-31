dict = {
    "key" : 3,
    "mace" : 1,
    "gold coin" : 24,
    "lantern" : 1,
    "stone" : 10
}

num = 0

print("Equipment:")

for a, b in dict.items():
    print(b, a)
    num += b

print("Total number of things:", num)