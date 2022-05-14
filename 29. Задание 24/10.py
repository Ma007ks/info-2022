from collections import Counter

s = open("10.txt").read()
print(Counter(s[i + 2] for i in range(len(s) - 2) if s[i] == s[i + 1]).most_common())

# print(Counter(s).most_common())


# for curr in alphabet:
#     count = 0
#     for prev in alphabet:
#         group = prev * 2 + curr
#         for i in range(len(s) - 2):
#             if s[i : i + 3] == group:
#                 count += 1
#     print(curr, count)
