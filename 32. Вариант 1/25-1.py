import re

for a in range(2, 20000):
    for n in range(2, 30):
        x = a ** n
        if 100_000_000 <= x <= 150_000_000:
            # x = "*7??1*3?"
            # x = "*1?2??2*5"
            # * → \d*
            # ? → \d
            s = str(x)
            # if re.fullmatch(r"\d*7\d\d1\d*3\d", s):
            if re.fullmatch(r"\d*1\d2\d\d2\d*5", s):
                print(x, a, n)
