from functools import cache


def is_square(x):
    if x <= 0:
        return False
    return int(x ** 0.5) ** 2 == x


@cache
def is_square(x):
    y = 1
    while y ** 2 < x:
        y += 1
    return y ** 2 == x


def is_square(x):
    return x > 0 and x ** 0.5 % 1 == 0


nums = [int(x) for x in open("3.txt")]
sums = []

for i in range(len(nums) - 1):
    if is_square(nums[i]) or is_square(nums[i + 1]):
        sums.append(nums[i] + nums[i + 1])

print(len(sums))
print(min(sums))
