nums = [int(x) for x in open("17.txt")]

min_even = min(x for x in nums if x % 2 == 0)
# min_even = 824
#
# count = 0
#
# for i in range(len(nums) - 1):
#     a = nums[i]
#     b = nums[i + 1]
#     if (a % 5 == 0 and b % 5 != 0) or (a % 5 != 0 and b % 5 == 0):
#         if abs(a - b) < min_even:
#             count += 1
#             print(count, a, b)

count = 0
max_abs_diff = 0

# for i in range(len(nums) - 1):
#     a = nums[i]
#     b = nums[i + 1]

for a, b in zip(nums, nums[1:]):
    # if (a % 5 == 0 and b % 5 != 0) or (a % 5 != 0 and b % 5 == 0):
    if (a % 5 == 0) + (b % 5 == 0) == 1:
        abs_diff = abs(a - b)
        if abs_diff < min_even:
            count += 1
            max_abs_diff = max(abs_diff, max_abs_diff)

print(count)
print(max_abs_diff)
