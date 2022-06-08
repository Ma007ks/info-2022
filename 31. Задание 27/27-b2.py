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

for station in range(1, n):
    old_neg = ns.pop(0)  # elements[station - 1 + n // 2]
    old_pos = ps.pop(0)  # elements[station - 1]
    ns.append(old_pos)
    ps.append(old_neg)
    p_sum = p_sum - old_pos + old_neg
    n_sum = n_sum - old_neg + old_pos
    tp = tp - n_sum + p_sum
    if tp < min_tp:
        min_tp = tp
        print(station, min_tp)

print(min_tp)
