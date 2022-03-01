s = "122" * 250

while "22" in s or "1111" in s:
    if "1111" in s:
        s = s.replace("1111", "21", 1)
    if "22" in s:
        s = s.replace("22", "11", 1)

print(s)
