def is_prime(x):
    factors = [f for f in range(1, x + 1) if x % f == 0]
    return len(factors) == 2


nums = [int(x) for x in open("12.txt")]
count = 0
min_element = +100000000000
max_element = -100000000000

for a, b, c in zip(nums, nums[1:], nums[2:]):
    if is_prime(a) and is_prime(b) and is_prime(c):
        count += 1
        min_element = min(min_element, a, b, c)
        max_element = max(max_element, a, b, c)

print(count, max_element - min_element)
