from functools import cache


@cache
def gm(x, y):
    if x + y >= 259:
        return "end"

    ls = {gm(x + 1, y), gm(x, y + 1), gm(x * 2, y), gm(x, 2 * y)}

    if "end" in ls:
        return "В1"
    if "П1" in ls:
        return "В2"
    if "П2" in ls:
        return "В3"

    if ls == {"В1"}:
        return "П1"
    if ls == {"В2"}:
        return "П2"
    if ls == {"В1", "В2"}:
        return "П1-2"


# for s in range(1, 242):
#     print(s, gm(17, s))

for s in range(1, 242):
    x, y = 17, s
    ls = {gm(x + 1, y), gm(x, y + 1), gm(x * 2, y), gm(x, 2 * y)}
    if "В1" in ls:
        print(s)
