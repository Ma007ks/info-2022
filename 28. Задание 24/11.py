s = open("Файлы/11.txt").read()

s = s.replace("XZZY", "XZZ ZZY")

for w in s.split():
    if len(w) >= 1000:
        print(len(w), w)
