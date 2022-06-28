nums = [int(x) for x in open("17.txt")]

mn = min(nums)
count = 0

for a, b in zip(nums, nums[1:]):
    if a % 117 == mn or b % 117 == mn:
        count += 1
        if a + b >= 10000:
            print(a + b)

print(count)