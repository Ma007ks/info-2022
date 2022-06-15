n, *nums = [int(x) for x in open("27-b.txt")]

m = 999

counts = [0] * m
count = 0

for x in nums:
    y = (m - x % m) % m  # индекс напарника
    counts = counts[y:] + counts[:y]  # сдвиг
    counts[x % m] += 1
    count += counts[0]  # обновление количества

print(count)
