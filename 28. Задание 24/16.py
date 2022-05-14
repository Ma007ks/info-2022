s = "xxxyxyyxxxxxxxxxyyyyyxxxxxxyyyy"
# print(s)
#
# s = s.replace("xy", "xy xy")
# print(s)
#
# s = s.replace("yx", "yx yx")
# print(s)
#
# for w in s.split():
#     if w[0] == w[-1] and len(w) >= 20:
#         print(w)

for m in "klmnop":
    for n in "klmnop":
        if m != n:
            for k in range(1, 1000):
                if n + k * m + n in s:
                    if k >= 100:
                        print(...)
