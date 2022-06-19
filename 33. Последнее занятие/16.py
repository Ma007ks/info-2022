s = open("24/1.txt").read()

s = s.replace("XZZY", "XZZ ZZY")
groups = s.split()

for g in groups:
    if len(g) > 1500:
        print(len(g), g)
