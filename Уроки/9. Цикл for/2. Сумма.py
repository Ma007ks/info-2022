lst = [25, 12, 15, 20, 4, 7, 8]

# print(sum(lst))

s = 0  # s — переменная, в которую мы будем считать сумму

# Посчитать сумму нечётных элементов списка

for x in lst:
    if x % 2 == 1:
        s += x

print(s)
