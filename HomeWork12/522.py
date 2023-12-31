string = "google"
string2 = {}

for i in string:
    string2[i] = string2.get(i, 0) + 1

for key, value in string2.items():
    print(f"{key} {value}")