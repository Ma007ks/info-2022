nums = list(map(int, open("11.txt")))

# count = 0
# min_abs_product = float("inf")
products = []

for a, b, c in zip(nums, nums[1:], nums[2:]):
    if a < b < c and a % 10 == 5:
        products.append(abs(a * b * c))
        # count += 1
        # min_abs_product = min(min_abs_product, abs(a * b * c))
        # min_abs_product = abs(a * b * c)
        # if min_abs_product <= 200000:
        #     print(min_abs_product)

# print(count, min_abs_product)
print(len(products), min(products))
