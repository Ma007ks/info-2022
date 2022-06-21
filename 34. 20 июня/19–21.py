def gm(s):
    if s >= 129:
        return "end"

    ls = {gm(s + 1), gm(s * 2)}

    # Победные позиции
    if "end" in ls:
        return "В1"
    if "П1" in ls:
        return "В2"
    if "П2" in ls:
        return "В3"

    # Проигрышные позиции
    if ls == {"В1"}:
        return "П1"
    if ls == {"В2"}:
        return "П2"
    if ls == {"В1", "В2"}:
        return "П1-2"


for s in range(1, 129):
    print(s, gm(s))
