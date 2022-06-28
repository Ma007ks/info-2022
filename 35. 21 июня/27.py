labs = dict([int(v) for v in line.split()] for line in open("27-a.txt"))

for l in labs:
    p = labs[l]
    labs[l] = p // 36 if p % 36 == 0 else p // 36 + 1

nums = sorted(labs)
min_result = 1000000000000000000

for b in nums[::10]:
    # if 40146873 <= b <= 60238770:
    # if 49213142 <= b <= 51202350:
    # if 49905064 <= b <= 50104067:
    # if 49965031 <= b <= 49987382:
    if 49973108 <= b <= 49975189:
        result = sum(abs(b - l) * labs[l] for l in labs)
        print(b, result)
