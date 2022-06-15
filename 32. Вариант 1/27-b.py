n, *nums = [int(x) for x in open("27-a.txt")]

count = 0

for s in range(n):
    for f in range(s, min(n, s + 100)):
        sequence = nums[s : f + 1]
        if sum(sequence) % 999 == 0:
            count += 1

    if s % 10000 == 0:
        print(s)

print(count)

# Неправильное количество (<= 100 элементов): 188558
# Правильное количество (правильная программа): 188558
