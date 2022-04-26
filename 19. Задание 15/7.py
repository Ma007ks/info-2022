for a in range(1, 1000):
    if all(not ((120 % a == 0) <= (168 % a != 0)) for x in range(1, 10000)):
        print(a)
