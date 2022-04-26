def q(s, f):
    # sd — sum_digits — сумма цифр числа s
    # sd = s // 10 + s % 10
    # sd = sum(int(d) for d in str(s))
    sd = sum(map(int, str(s)))
    return q(s + 1, f) + q(s + sd, f) if s < f else s == f


print(q(1, 15))
