nums = [int(line) for line in open("1.txt")]
# nums = list(map(int, open("1.txt")))

count = 0
max_sum = -1000000

for a, b in zip(nums, nums[1:]):
    if a % 3 == 0 and b % 3 == 0:
        count += 1
        max_sum = max(max_sum, a + b)

print(count)
print(max_sum)
