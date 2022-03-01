from itertools import combinations

s = "1" * 10 + "2" * 4


def unique_permutations(s):
    count_2 = s.count("2")
    count = len(s)
    for c in combinations(range(count), count_2):
        new_s = "".join("2" if i in c else "1" for i in range(count))
        yield new_s


count = 0

for x in unique_permutations(s):
    count += 1
    print(x)

print(count)
# lst = list(s)
# max_sum = 0
#
# while True:
#     shuffle(lst)
#     s = "".join(lst)
#
#     while "11" in s:
#         if "112" in s:
#             s = s.replace("112", "6", 1)
#         else:
#             s = s.replace("11", "3", 1)
#
#     sm = sum(int(d) for d in s)
#     if sm >= max_sum:
#         print(sm, "".join(lst))
#         max_sum = sm
