# nums = [int(x) for x in open("5.txt")]
nums = list(map(int, open("5.txt")))

min_21 = min(x for x in nums if x % 21 == 0)

count = 0

for a, b in zip(nums, nums[1:]):
    if a % min_21 == 0 or b % min_21 == 0:
        count += 1
        if a + b >= 170000:
            print(a + b)

print(count)
