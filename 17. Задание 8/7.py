from itertools import product

i = 0
for w in product("ABX", repeat=6):
    w = "".join(w)
    if w.count("X") == 1:
        i += 1
        print(i, w)
