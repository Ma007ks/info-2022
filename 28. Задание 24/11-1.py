s = open("Файлы/11.txt").read()

for w in s.split("XZZY"):
    if len(w) >= 1000:
        print(len(w), w)
