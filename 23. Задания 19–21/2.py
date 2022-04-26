from functools import cache


@cache
def gm(x, prev_move=0):
    if x >= 34:
        return "end"

    # ls = [gm(x + 1, 1), gm(x + 2, 2), gm(x * 2, 3)]
    # if 1 <= prev_move <= 3:
    #     del ls[prev_move - 1]
    # ls = set(ls)

    if prev_move == 1:
        ls = {gm(x + 2, 2), gm(x * 2, 3)}
    elif prev_move == 2:
        ls = {gm(x + 1, 1), gm(x * 2, 3)}
    elif prev_move == 3:
        ls = {gm(x + 1, 1), gm(x + 2, 2)}
    else:
        ls = {gm(x + 1, 1), gm(x + 2, 2), gm(x * 2, 3)}

    if "end" in ls:
        return "В1"

    if ls == {"В1"}:
        return "П1"

    if "П1" in ls:
        return "В2"

    if ls == {"В2"}:
        return "П2"


for s in range(1, 34):
    print(s, gm(s))
