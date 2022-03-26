for n in range(1000, 10000):
    a, b, c, d = map(int, str(n))
    ls = [a + b, b + c, c + d]
    ls.sort()
    # r = int(str(ls[1]) + str(ls[0]))
    r = int(f"{ls[1]}{ls[0]}")
    if r == 127:
        print(n)

# sn = str(n)
# a = int(sn[0])  # тысячи
# b = int(sn[1])  # сотни
# c = int(sn[2])  # десятки
# d = int(sn[3])  # единицы

# a = n // 1000
# b = n // 100 % 10
# c = n // 10 % 10
# d = n % 10
