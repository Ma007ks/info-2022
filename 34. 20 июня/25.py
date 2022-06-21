# unique = set()
#
# for i in range(1000000):
#     s = "123" + str(i)[1:] + "67"
#     x = int(s)
#     if x % 123 == 0 and x <= 10 ** 8:
#         unique.add(x)
#
#
# for x in sorted(unique):
#     print(x, x / 123)

# for x in range(10 ** 8 + 1):
#     s = str(x)
#     if x % 123 == 0 and s[:3] == "123" and s[-2:] == "67":
#         print(x, x / 123)

import re

# * — \d*
# ? — \d

for x in range(10 ** 8 + 1):
    if x % 123 == 0 and re.fullmatch("123\d*67", str(x)):
        print(x, x / 123)