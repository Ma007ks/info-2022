s = "0" + "1" * 12 + "2" * 15 + "3" * 17
# s = f"0{'1' * 12}{'2' * 15}{'3' * 17}"

print(s)
while "01" in s or "02" in s or "03" in s:
    s = s.replace("01", "20", 1)
    print(s)
    s = s.replace("02", "120", 1)
    print(s)
    s = s.replace("03", "302", 1)
    print(s)
