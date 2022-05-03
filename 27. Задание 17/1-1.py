# nums = list(map(int, open("1.txt")))
nums = [3, 3, 6, 7, 2, 18, 27, 45]
# print(sum(nums[i] % 3 == 0 and nums[i + 1] % 3 == 0 for i in range(len(nums) - 1)))
print(sum(a % 3 == 0 and b % 3 == 0 for a, b in zip(nums, nums[1:])))
print(max(a + b for a, b in zip(nums, nums[1:]) if a % 3 == 0 and b % 3 == 0))

sums = [a + b for a, b in zip(nums, nums[1:]) if a % 3 == 0 and b % 3 == 0]
print(len(sums), max(sums))
