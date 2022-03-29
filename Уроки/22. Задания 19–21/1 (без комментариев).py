from functools import cache


@cache
def gm(x, y):
    if x + y >= 142:
        return "end"
    ls = {gm(x + 2, y), gm(x * 2, y), gm(x, y + 2), gm(x, y * 2)}

    if "end" in ls:
        return "В1"
    if ls == {"В1"}:
        return "П1"
    if "П1" in ls:
        return "В2"
    if ls == {"В1", "В2"}:
        return "П1-2"


# for s in range(1, 139):
#     print(s, "—", gm(2, s))

for s in range(1, 139):
    # (2, s) → (4, s), (2, s + 2), (2, 2 * s)
    # if gm(4, s) == "В1" or gm(2, s + 2) == "В1" or gm(2, 2 * s) == "В1":
    if "В1" in {gm(4, s), gm(2, s + 2), gm(2, 2 * s)}:
        print(s)
