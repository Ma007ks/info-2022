# 1. Промежуток
# 2. Маска
# 3. Степень

for a in range(2, 20000):
    for n in range(2, 30):
        x = a ** n
        if 120_000_000 <= x <= 122_500_000:
            s = str(x)
            if "50" in s:
                first_index = s.index("50")
                if "2" in s[first_index + 2 :]:
                    print(x, first_index, s[first_index + 2 :])

"""
120450625 10975 2
121506529 11023 2
121550625 105 4
121705024 11032 2
"""
