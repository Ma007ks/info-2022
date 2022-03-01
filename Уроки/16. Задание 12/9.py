s = "121112121212111"

while "12" in s:
    s = s.replace("12", "4", 1)

print(s, sum(int(d) for d in s))
