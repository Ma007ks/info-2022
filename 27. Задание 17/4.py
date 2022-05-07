nums = [int(x) for x in open("4.txt")]

max_3 = max(x for x in nums if x % 3 == 0)
# count = max_sum = 0
sums = []

for a, b in zip(nums, nums[1:]):
    if (a % 3 == 0 or b % 3 == 0) and a + b <= max_3:
        sums.append(a + b)
        # count += 1
        # max_sum = max(max_sum, a + b)

sums = [
    nums[i] + nums[i + 1]
    for i in range(len(nums) - 1)
    if (nums[i] % 3 == 0 or nums[i + 1] % 3 == 0) and nums[i] + nums[i + 1] <= max_3
]
# print(count, max_sum)
print(len(sums), max(sums))
