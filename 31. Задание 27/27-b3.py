"""
    0 1  2 3  4 5
    8 20 5 13 7 19

    station = 0: 0 * 8 + 1 * 20 + 2 * 5 + 3 * 13 + 2 * 7 + 1 * 19 = 102: (8, 20, 5), (13, 7, 19)
    station = 1: 0 * 20 + 1 * 5 + 2 * 13 + 3 * 7 + 2 * 19 + 1 * 8 = 98 = 102 - 20 - 5 - 13 + 7 + 19 + 8: (20, 5, 13), (7, 19, 8)
    station = 2: 0 * 5 + 1 * 13 + 2 * 7 + 3 * 19 + 2 * 8 + 1 * 20 = 120 = 98 - 5 - 13 - 7 + 19 + 8 + 20: (5, 13, 7), (19, 8, 20)
"""

n, *elements = map(int, open("27-b.txt"))
# n, elements = 6, [8, 20, 5, 13, 7, 19]

ps = elements[n // 2 :]
ns = elements[: n // 2]

p_sum = sum(ps)
n_sum = sum(ns)

negative_answer = sum(ns[i] * i for i in range(n // 2))
positive_answer = sum(ps[i] * (n // 2 - i) for i in range(n // 2))

tp = negative_answer + positive_answer
min_tp = tp

init_diff = p_sum - n_sum

for station in range(1, n):
    new_pos = elements[station - 1]
    new_neg = elements[(station + n // 2 - 1) % n]
    diff = new_pos - new_neg
    p_sum = p_sum + diff
    n_sum = n_sum - diff
    tp = tp + p_sum - n_sum
    if tp < min_tp:
        min_tp = tp

print(min_tp)
