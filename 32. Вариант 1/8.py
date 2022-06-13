count = 0

for a in range(5):
    for b in range(5):
        for c in range(5):
            if a > b > c:
                count += 1
                print(count, f"{a}{b}{c}")
