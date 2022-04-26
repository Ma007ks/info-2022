lst = []

for x in range(1, 10):
    if x % 3 == 2:
        for y in range(1, 5):
            lst.append(x * y)

new_lst = [x * y for x in range(1, 10) if x % 3 == 2 for y in range(1, 5)]

print(lst)
print(new_lst)
