i = 0

# a % 2 == 1 or b % 2 == 1 or c % 2 == 1 or d % 2 == 1 or e % 2 == 1 or f % 2 == 1


for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        if any(x % 2 == 1 for x in (a, b, c, d, e, f)):
                            i += 1

print(i)
