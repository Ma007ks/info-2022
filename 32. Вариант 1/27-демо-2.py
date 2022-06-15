# n, *nums = [int(x) for x in open("27_A.txt")]

nums = [2, 7, 2, 4, 6, 2, 5, 3, 4, 2, 2, 3]

k = 4

sums = [0] * k
lens = [0] * k

for x in nums:
    for i in range(k):
        if lens[i] != 0 or i == 0:
            sums[i] += x
            lens[i] += 1

    brother = (k - x % k) % k
    sums = sums[brother:] + sums[:brother]
    lens = lens[brother:] + lens[:brother]

    if sums[0] >= 744080213:
        print(sums[0], lens[0])
