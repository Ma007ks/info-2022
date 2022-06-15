n, *nums = [int(x) for x in open("27-b.txt")]

m = 999
d = 100

counts = [0] * m
buffer = nums[:d]

count = 0

for x in nums[d:]:
    buffer.append(x)

    # Самый старый элемент покидает буфер
    old_element = buffer.pop(0)

    # И обновляет таблицу
    y = (m - old_element % m) % m  # индекс напарника
    counts = counts[y:] + counts[:y]  # сдвиг
    counts[old_element % m] += 1

    # Обновление количества
    buffer_brother = (m - sum(buffer) % m) % m  # напарник для буфера
    count += counts[buffer_brother]  # обновление количества

print(count)
