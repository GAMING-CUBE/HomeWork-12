dict = {
    "Avengers: Endgame" : 2019,
    "Iron Man" : 2008,
    "Guardians of the Galaxy" : 2014,
    "Thor" : 2011
}

list = []

for i in dict.keys():
    list.append(i)

list = sorted(list)

sorted_dict = {}

for i in list:
    if i in dict.keys():
        elem = dict.get(i)
        sorted_dict.update({i : elem})

print(sorted_dict)