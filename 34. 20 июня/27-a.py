labs = [[int(v) for v in line.split()] for line in open("27-a.txt")]
labs_with_bags = [[l, p // 38 if p % 38 == 0 else p // 38 + 1] for l, p in labs]

min_result = 1000000000000

for i in range(50300, 50500, 10):
    result = sum(abs(i - l) * b for l, b in labs_with_bags)
    if result < min_result:
        print(i, result)
        min_result = result
