n, *nums = [int(x) for x in open("27-a.txt")]

m = 999

counts = [1] + [0] * (m - 1)
count = 0

for x in nums:
    y = (m - x % m) % m  # индекс напарника
    count += counts[y]  # обновление количества
    counts = counts[y:] + counts[:y]  # сдвиг
    counts[0] += 1

print(count)
