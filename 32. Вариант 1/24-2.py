s = open("24.txt").read()

g = ""

max_count = 0

for c in s:
    g += c
    if len(g) == 1:
        continue
    if len(g) == 2 and g[0] != g[1]:
        continue
    if len(g) > 2 and g[-1] == g[-2]:
        continue
    if len(g) > 2 and g[-1] == g[0]:
        if len(g) > 8:
            print(g)

    g = g[-2:]
