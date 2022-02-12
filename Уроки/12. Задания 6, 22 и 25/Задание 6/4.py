for i in range(1, 500):
    # print("Проверяем", i)
    s = i  # s = int(input())
    n = 1
    count_iterations = 0  # сколько итераций сделал основной цикл
    while s * n < 4096:
        s //= 2
        n *= 4
        # Проверка зацикливания:
        count_iterations += 1
        if count_iterations > 100000:
            break

    if count_iterations > 100000:
        print("Зацикливание произошло на", i)

    if n == 1024:
        print(i)  # print(n)
