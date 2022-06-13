for i in range(1, 1000000):
    try:
        k = i // (i % 5)
        s = 0
        n = 40

        while s <= n ** 3:
            s += k
            n += 1
            if n >= 1000:
                break

        if n == 42:
            print(i)
    except:
        print(f"Произошла ошибка на числе {i}")
