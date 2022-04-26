from functools import cache


@cache
def gm(x, y):
    if x + y >= 77:
        return "end"

    ls = {
        gm(x + 1, y),
        gm(x, y + 1),
        gm(x + 2 * y, y),
        gm(x, y + 2 * x),
    }

    if "end" in ls:
        return "В1"

    if ls == {"В1"}:
        return "П1"

    if "П1" in ls:
        return "В2"

    if ls == {"В1", "В2"}:
        return "П1-2"


for s in range(1, 68):
    # if gm(9, s) == "В2":
    #     print(s)
    # if gm(9, s) == "П1-2":
    #     print(s)
    print(s, gm(9, s))
    # if (
    #     gm(10, s) == "В1"
    #     or gm(9, s + 1) == "В1"
    #     or gm(9, s + 18) == "В1"
    #     or gm(9 + 2 * s, s) == "В1"
    # ):
    #     print(s)

    # if "В1" in {gm(10, s), gm(9, s + 1), gm(9, s + 18), 9 + 2 * s, s}:
    #     print(s)
