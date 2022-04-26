lines = open("5.txt").read().splitlines()
count = int(lines.pop(0))

pairs = [[int(v) for v in line.split()] for line in lines]
# pairs = [list(map(int, line.split())) for line in lines]

pairs = []
for line in lines:
    a, b = line.split()
    pairs.append([int(a), int(b)])

print(count)
print(pairs[:10])
