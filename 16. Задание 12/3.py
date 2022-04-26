s = "00" * 108 + "35" * 108

while "00000" in s or "353535" in s or "5555" in s:
    if "00000" in s:
        s = s.replace("00000", "8", 1)
    if "888" in s:
        s = s.replace("888", "880", 1)
    if "5555" in s:
        s = s.replace("555", "3535", 1)
    elif "3535" in s:
        s = s.replace("3535", "5", 1)

print(s)
