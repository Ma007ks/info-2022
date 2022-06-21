from random import randrange

with open("27-a.txt", "w") as file:
    print(1000, file=file)
    distances = set()
    for _ in range(1000):
        d = randrange(1, 10 ** 5 + 1)
        while d in distances:
            d = randrange(1, 10 ** 5 + 1)
        print(d, randrange(1, 1000), file=file)
