nums = [int(line) for line in open("2.txt")]

diffs = []

for a, b in zip(nums, nums[1:]):
    if a % 10 == 5 and str(b)[-1] == "5":
        diffs.append(abs(a - b))

print(len(diffs))
print(max(diffs))
