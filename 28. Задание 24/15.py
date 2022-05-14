s = open("Файлы/14.txt").read()

for x in range(10):
    for y in range(10):
        if x < y:
            s = s.replace(f"{x}{y}", f"{x} {y}")
            s = s.replace(f"{x}{y}", f"{x} {y}")

for w in s.split():
    if len(w) > 10:
        print(len(w), w)
