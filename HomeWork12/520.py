string = "The quick brown FOX jumps over a lazy DOG"
upper = 0
lower = 0

for i in string:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

print("UPPER CASE", upper)
print("LOWER CASE", lower)