s = open("1.txt").read()

max_length = 0

for c in "%!?":
    length = 1
    while c * length in s:
        max_length = max(max_length, length)
        length += 1

print(max_length)
