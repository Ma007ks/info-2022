n, *nums = [int(x) for x in open("27-a.txt")]

count = 0

for s in range(n):
    for f in range(s + 100, n):
        sequence = nums[s : f + 1]
        if sum(sequence) % 999 == 0:
            count += 1

print(count)
