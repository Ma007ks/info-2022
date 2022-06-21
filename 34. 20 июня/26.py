n, *nums = [int(x) for x in open("26.txt")]

nums.sort(reverse=True)

count = 1
min_box = nums[0]

for i in range(1, n):
    if min_box - nums[i] >= 5:
        min_box = nums[i]
        count += 1
        print(count, min_box)
