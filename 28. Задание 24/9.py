s = open("Файлы/9.txt").read()

s = s.replace("PP", "P P")
s = s.replace("PP", "P P")

for w in s.split():
    if len(w) > 180:
        print(len(w), w)
