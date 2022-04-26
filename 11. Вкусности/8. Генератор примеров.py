from random import randrange

for _ in range(50):
    numbers = [randrange(1, 11) for _ in range(randrange(3, 11))]
    print(" + ".join(str(n) for n in numbers), "=", sum(numbers))
