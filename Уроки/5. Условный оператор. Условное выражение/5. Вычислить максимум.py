x, y = 70, 70

# Записать в переменную m максимальное число из чисел x и y, а затем вывести m.
# m = max(x, y)

if x >= y:
    m = x
else:
    m = y

print(m)

# Другой вариант:
m = x
if y > x:
    m = y

print(m)

# x, y, z = 3, 7, 2
#
# m = x
# if y > m:
#     m = y
# if z > m:
#     m = z
