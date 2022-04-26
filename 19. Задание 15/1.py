def expr(x, y, a):
    return ((x < a) <= (x ** 2 < 100)) and ((y ** 2 <= 64) <= (y <= a))


for a in range(-1000, 1000):
    # Проверяем конкретную a-шку:
    # перебираем всевозможные значения x и y
    # и смотрим, получается ли всегда истина.
    # Если найдётся нарушитель (какая-то парочка x и y),
    # то такая a-шка не подойдёт

    # result = True
    # for x in range(1000):
    #     for y in range(1000):
    #         if not expr(x, y, a):
    #             result = False

    if all(expr(x, y, a) for x in range(200) for y in range(200)):
        print(a)
