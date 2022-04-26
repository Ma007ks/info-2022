for a in range(1000):
    if all(
        (y >= a) or (x > a) or (x * y < 100) for x in range(1000) for y in range(1000)
    ):
        print(a)
