count = 0

for i in range(1, 1000):
    x = i
    n = 10
    while x < 500:
        x = x + n
        n = n + 6
    if n == 40:
        count += 1
        print(count, "—", i)

print(count)
