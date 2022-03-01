s = "1" * 105

while "11" in s or "2222" in s:
    if "2222" in s:
        s = s.replace("2222", "1", 1)
    if "11" in s:
        s = s.replace("11", "222", 1)
    print(s)
