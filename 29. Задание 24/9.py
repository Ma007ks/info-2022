s = open("9.txt").read()

# good_strings = [
#     sb for i in range(len(s)) if len(sb := s[i : i + 4]) == 4 and len(set(sb)) == 4
# ]

# good_strings = []
# for i in range(len(s) - 3):
#     a, b, c, d = sub = s[i : i + 4]
#     # if a != b and a != c and a != d and b != c and b != d and c != d:
#     if len(set(sub)) == 4:
#         good_strings.append(sub)
#
# print(x := sum("e" in x for x in good_strings))
# print(y := sum("d" in x for x in good_strings))
# print(x - y)

count = 0

for i in range(len(s) - 3):
    sub = s[i : i + 4]
    if len(set(sub)) == 4 and "d" in sub:
        count += 1

print(count)
