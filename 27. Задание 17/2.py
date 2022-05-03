nums = [int(line) for line in open("2.txt")]

count = 0
max_value = 0

for a, b in zip(nums, nums[1:]):
    if a % 10 == 5 and str(b)[-1] == "5":
        count += 1
        max_value = max(max_value, abs(a - b))

print(count, max_value)
