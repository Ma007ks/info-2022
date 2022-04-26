# for x in range(1, 100000):
#     fs = [i for i in range(2, x) if x % i == 0]
#     if len(fs) == 3:
#         print(x, fs)

# p^4

# p = 2, 3, 5, 7, 11, 13, 17
# p = 16. Задание 12, 81, 625, ...

for p in range(1, 1000):
    fs = [i for i in range(1, p + 1) if p % i == 0]
    if len(fs) == 2 and 289_123_456 <= p ** 4 <= 389_123_456:
        print(p, p ** 4, p ** 3)
