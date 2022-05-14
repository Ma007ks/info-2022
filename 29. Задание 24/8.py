s = open("8.txt").read()

print(s.count("#@@"))

count = 0

for i in range(len(s)):
    if s[i : i + 3] == "#@@":
        count += 1

print(count)
