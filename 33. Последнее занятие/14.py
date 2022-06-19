s = open("24/1.txt").read()

length = 1713

for i in range(len(s) - length):
    substring = s[i : i + length]
    if "XZZY" not in substring:
        print(len(substring), substring)
