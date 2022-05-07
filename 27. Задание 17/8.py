nums = [int(x) for x in open("8.txt")]

# for i in range(len(nums) - 2):
#     a, b, c = nums[i], nums[i + 1], nums[i + 2]

sums = []

for a, b, c in zip(nums, nums[1:], nums[2:]):
    if max(a, b, c) > 0:
        sums.append(a + b + c)

print(len(sums), max(sums))
