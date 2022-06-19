import re

# ? — \d
# * — \d*

# 15?2*240*2
# должны делиться на 13 и 7
# первые 5 самых маленьких

for x in range(123450708, 123460708):
    if x % 23 == 0 and re.fullmatch(r"12345\d7\d8", str(x)):
        print(x, x / 23)
