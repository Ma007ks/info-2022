i = 0

for x in range(100000):
    s = str(x)
    if len(set(s)) == len(s) and x % 4 == 0:
        rems = "".join(str(int(d) % 2) for d in s)
        if "00" not in rems and "11" not in rems:
            i += 1
            print(i, x, rems)
