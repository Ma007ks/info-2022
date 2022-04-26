lines = open("3.txt").read().splitlines()

print(max(len(line) for line in lines))
print(min(len(line) for line in lines))
print(max(line.count("X") for line in lines))
print(max(line.count("x") for line in lines))

max_count_x = 0

for line in lines:
    max_count_x = max(max_count_x, line.count("X"))

print(max_count_x)

print(sum(len(line) == 1 for line in lines))
print([line for line in lines if len(line) == 1])

print([line for line in lines if line == line[::-1]])

print([line for line in lines if len(set(line.lower())) == len(line)])
