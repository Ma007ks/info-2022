def gm(x):
    if x >= 22:
        return "end"

    ls = {gm(x + 1), gm(x + 2)}
    if x % 2 == 1:
        ls.add(gm(x * 2))

    if "end" in ls:
        return "В1"
    if ls == {"В1"}:
        return "П1"
    if "П1" in ls:
        return "В2"
    if ls == {"В1", "В2"}:
        return "П1-2"
    if "П1-2" in ls:
        return "В2-3"


for s in range(1, 22):
    print(s, gm(s))
