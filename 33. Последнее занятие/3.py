for i in range(1, 2000):
    # print("Проверяем", i)
    k = i
    k = k // 25

    a = 0
    b = 2 ** 10

    count = 0

    while a <= b:
        a += k
        k -= 1
        b += 1
        count += 1
        if count > 10000:
            break
    if b == 1049:
        print(i)
