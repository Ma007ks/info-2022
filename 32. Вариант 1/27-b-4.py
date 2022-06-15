n, *nums = [int(x) for x in open("27-b.txt")]

m, d = 999, 100

counts = [0] * m
buffer = nums[:d]
count = 0

for x in nums[d:]:
    buffer.append(x)
    old_element = buffer.pop(0)
    y = (m - old_element % m) % m  # индекс напарника
    counts = counts[y:] + counts[:y]  # сдвиг
    counts[old_element % m] += 1
    buffer_brother = (m - sum(buffer) % m) % m  # напарник для буфера
    count += counts[buffer_brother]  # обновление количества

print(count)
