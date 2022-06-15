n, *nums = [int(x) for x in open("27_B.txt")]

k = 43

sums_lengths = [(0, 0)] * 43

for x in nums:
    sums_lengths = [
        (sums_lengths[i][0] + x, l + 1)
        if (l := sums_lengths[i][1]) != 0 or i == 0
        else (0, 0)
        for i in range(k)
    ]
    brother = (k - x % k) % k
    sums_lengths = sums_lengths[brother:] + sums_lengths[:brother]
    if sums_lengths[0][0] >= 744080213:
        print(sums_lengths[0])
