nums = [int(x) for x in open("10.txt")]

count = 0
elements = []

# for left, x, right in zip(nums, nums[1:], nums[2:]):
for i in range(1, len(nums) - 1):
    x = nums[i]
    left = nums[i - 1]
    right = nums[i + 1]
    if x == left + right:
        elements.append(x)
        # count += 1
        # if x >= 500:
        #     print(x)

print(len(elements), max(elements))
