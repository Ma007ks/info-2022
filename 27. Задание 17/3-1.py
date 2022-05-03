nums = [int(x) for x in open("3.txt")]

# squares = [x ** 2 for x in range(1, 101)]
squares = {x ** 2 for x in range(1, 101)}

sums = []
for a, b in zip(nums, nums[1:]):
    if a in squares or b in squares:
        sums.append(a + b)

print(len(sums))
print(min(sums))
