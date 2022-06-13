for n in range(2, 1000):
    sn = str(n)
    se = sum(int(d) for d in sn if d in "02468")
    # sp = 0
    # for i in range(len(sn)):
    #     p = i + 1
    #     if p % 2 == 0:
    #         sp += int(sn[i])
    # for p, d in enumerate(sn, start=1):
    #     if p % 2 == 0:
    #         sp += int(d)
    # sp = sum(int(d) for p, d in enumerate(sn, start=1) if p % 2 == 0)
    sp = sum(int(d) for d in sn[1::2])
    if abs(se - sp) == 9:
        print(n)
        break
