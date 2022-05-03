nums = [25, 10, -4, 7, 9, 0, 5, -10, -17, 13]

# nums =        [25, 10, -4, 7, 9, 0, 5, -10, -17, 13]
# nums[1:] =    [10, -4, 7, 9, 0, 5, -10, -17, 13]

# (25, 10)
# (10, -4)
# (-4, 7)
# ...
# 9: (-17, 13)

# for i in range(len(nums) - 1):
#     a, b = nums[i], nums[i + 1]
#
# for a, b in zip(nums, nums[1:]):
#     print(a, b)
#
# for i in range(len(nums) - 2):
#     a, b, c = nums[i], nums[i + 1], nums[i + 2]
#     print(a, b, c)

# for a, b, c in zip(nums, nums[1:], nums[2:]):
#     print(a, b, c)

# for number in nums:
#     print(number)

# for i in range(len(nums)):
#     print(nums[i])

for i, number in enumerate(nums):
    print(i, number)
