from random import randrange

with open("26.txt", "w") as file:
    print(10000, file=file)
    for _ in range(10000):
        print(randrange(1, 10 ** 5), file=file)
