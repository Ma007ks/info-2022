nums = [int(line) for line in open("1.txt")]
# nums = list(map(int, open("1.txt")))

for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    if a % 3 == 0 and b % 3 == 0:
        if a + b >= 18000:
            print(a + b)
