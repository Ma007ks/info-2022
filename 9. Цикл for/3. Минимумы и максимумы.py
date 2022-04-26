lst = [-101, 25, 12, 15, 20, 4, 7, 8, 1]

# mn = lst[0]
mn = None

for x in lst:
    if x % 2 != 0:  # повстречали чётное число...
        continue
    if mn is None:  # оно первое?
        mn = x  # значит, оно на данный момент и есть минимальное
    elif x < mn:  # оно не первое, и если оно меньше mn, то...
        mn = x  # мы обновим mn

for x in lst:
    if x % 2 == 0 and (mn is None or x < mn):
        mn = x

print(mn)
