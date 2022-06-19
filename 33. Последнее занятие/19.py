import re

# ? — \d
# * — \d*

# 15?2*240*2
# должны делиться на 13 и 7
# первые 5 самых маленьких

# 15?2*240*2
# 15022402

# for x in range(15022402, 15000022402):
#     if x % 13 == 0 and x % 7 == 0:
#         if re.fullmatch(r"15\d2\d*240\d*2", str(x)):
#             print(x)

numbers = set()

for a in range(10):
    for b in "", *range(1000):
        for c in "", *range(1000):
            x = int(f"15{a}2{str(b)[1:]}240{str(c)[1:]}2")
            if x % 13 == 0 and x % 7 == 0:
                numbers.add(x)

numbers = sorted(numbers)

print(numbers[:5])

"""
152224072
153282402
1502240012
1502240922
1502624032
"""