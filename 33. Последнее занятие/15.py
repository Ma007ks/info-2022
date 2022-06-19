s = open("24 (Открытый вариант–2022).txt").read()

s = s.replace("AB", "x")
s = s.replace("CB", "x")

s = s.replace("A", " ")
s = s.replace("B", " ")
s = s.replace("C", " ")

groups = s.split(" ")

for g in groups:
    if len(g) > 60:
        print(len(g), g)
