s = open("2.txt").read()

for a in "0123456789":
    for b in "0123456789":
        if a != b:
            s = s.replace(f"{a}{b}", f"{a} {b}")
            # print(a, b, "           ", s[:50])

print(max(map(len, s.split())))
print(max(len(w) for w in s.split()))

for w in s.split():
    if len(w) >= 30:
        print(len(w), w)
