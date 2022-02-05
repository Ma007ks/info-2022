a = [1, 5, 7, 2, 4, 6]
b = [7, 2, 9, 10]

# c = [1, 5, 7, 2, 4, 6, 7, 2, 9, 10]
# c = a + b

# c = []
# for x in a:
#     c.append(x)
# for x in b:
#     c.append(x)

c = []

for lst in a, b:
    for x in lst:
        c.append(x)

print(c)
