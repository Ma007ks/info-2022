# def algo(n):
#     r = bin(n)[2:]
#     r += "00" if n % 2 == 0 else "10"
#     return int(r, 2)
#
#
# for n in range(1, 100):
#     print(n, algo(n))

for n in range(1, 100):
    r = bin(n)[2:]
    r += "00" if n % 2 == 0 else "10"
    r = int(r, 2)
    if r > 130:
        print(n)
        break
