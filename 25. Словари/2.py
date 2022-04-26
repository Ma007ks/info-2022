from collections import defaultdict, Counter

# numbers_by_digits_sum = {
#     1: [1, 10, 100, 1000],
#     2: [2, 11, 20, 101, 110, 200, 1001],
#     3: [3, 12, 21, ...],
# }

# nd = {}
counter = defaultdict(int)

for x in range(1, 1001):
    ds = sum(int(d) for d in str(x))
    counter[ds] += 1

new_counter = Counter(sum(int(d) for d in str(x)) for x in range(1, 1001))

print(new_counter)

# print(nd)
# print(counter)
