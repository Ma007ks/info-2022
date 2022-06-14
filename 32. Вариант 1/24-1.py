s = open("24.txt").read()

for a in "klmnop":
    for b in "klmnop":
        if a != b:
            s = s.replace(a + b, a + " " + b)

groups = s.split()

for a, b, c in zip(groups, groups[1:], groups[2:]):
    if a[-1] == c[0] and len(b) >= 9:
        print(a, b, c)
