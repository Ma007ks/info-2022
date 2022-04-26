for a in range(1, 1000):
    if all((x % a != 0) <= ((x % 54 == 0) <= (162 % x != 0)) for x in range(1, 10000)):
        print(a)
