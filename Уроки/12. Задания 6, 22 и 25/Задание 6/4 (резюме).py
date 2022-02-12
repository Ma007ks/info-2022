for i in range(1, 1000):
    s = i
    n = 1

    count_iterations = 0
    while s * n < 4096:
        s //= 2
        n *= 4
        count_iterations += 1
        if count_iterations > 10000:
            print("Зацикливание:", i)
            break

    if n == 1024:
        print(i)
