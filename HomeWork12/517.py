dict = {
    "Andriy Zakruzhiy" : "08/09/2001",
    "Cristiano Ronaldo" : "02/05/1985",
    "Lionel Messi" : "06/24/1987"
}
a = input()

if a in dict.keys():
    print(a + "'s birthday is", dict[a])