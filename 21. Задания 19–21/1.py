def game(x):
    if x >= 29:
        return "end"

    m, n = game(x + 1), game(x * 2)

    if "end" in [m, n]:
        return "В1"

    if m == "В1" and n == "В1":
        return "П1"

    if "П1" in [m, n]:
        return "В2"

    if "В1" in [m, n] and "В2" in [m, n]:
        return "П1–2"


for s in range(1, 29):
    print(s, game(s))
