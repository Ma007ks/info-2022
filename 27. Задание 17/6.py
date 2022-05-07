nums = [int(x) for x in open("6.txt")]

count = 0
min_sum = 100000000
max_element = 0

for a, b in zip(nums, nums[1:]):
    s = a ** 2 + b ** 2
    if s > 90 and s % 2 == 1:
        count += 1
        # if a + b < -19000:
        #     print(a, b, a + b)
        if a + b <= min_sum:
            min_sum = a + b
            max_element = max(a, b)

print(count, max_element, min_sum)
