for x in range(201, 220):
    s = "1" * x
    while "111" in s or "222" in s:
        s = s.replace("111", "22", 1)
        s = s.replace("222", "1", 1)
    print(x, s)
