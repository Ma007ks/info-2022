s = "123" * 123

# заменить(x, y) → s = s.replace(x, y, 1)
# нашлось(x) → x in s

while "12" in s or "23" in s or "31" in s:
    if "12" in s:
        s = s.replace("12", "23", 1)
    elif "31" in s:
        s = s.replace("31", "12", 1)
    elif "23" in s:
        s = s.replace("23", "1", 1)

print(s)
