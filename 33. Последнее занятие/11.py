nums = [int(x) for x in open("17/4.txt")]

odds = [x for x in nums if x % 2 == 1]
avg = sum(odds) / len(odds)
count = 0
max_sum = 0

for a, b in zip(nums, nums[1:]):
    if (a % 5 == 0 or b % 5 == 0) and (a < avg or b < avg):
        count += 1
        max_sum = max(max_sum, a + b)
        if a + b > 14800:
            print(a, b, a + b)

print(count)
print(max_sum)
