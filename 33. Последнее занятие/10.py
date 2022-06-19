nums = [int(x) for x in open("17/4.txt")]

odds = [x for x in nums if x % 2 == 1]
avg = sum(odds) / len(odds)
count = 0

for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    if (a % 5 == 0 or b % 5 == 0) and (a < avg or b < avg):
        count += 1
        if a + b > 14800:
            print(a, b, a + b)

print(count)
