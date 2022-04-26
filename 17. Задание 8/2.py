# i = 0
# for a in "АНП":
#     for b in "АНП":
#         for c in "АНП":
#             for d in "АНП":
#                 for e in "АНП":
#                     i += 1
#                     print(i, a + b + c + d + e)
from itertools import product

i = 0
for w in product("АНП", repeat=5):
    i += 1
    print(i, w)
