nums = list(map(int, open("7.txt")))

# count = 0
# max_element = 0
maximums = []

for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    if 100 <= abs(a) + abs(b) <= 700:
        maximums.append(max(a, b))
        # count += 1
        # max_element = max(max_element, a, b)

# print(count, max_element)
print(len(maximums), max(maximums))
