dict = {
    190 : "Jack",
    232 : "Alice",
    550 : "Bob"
}

for i in range(4):
    a = int(input())
    if a in dict.keys():
        print("Hi,", dict[a] + "!")
    else:
        print("Hi, to all!")