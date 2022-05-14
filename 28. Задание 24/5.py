s = open("Файлы/5.txt").read()

s = s.replace("00", "0 0")
s = s.replace("00", "0 0")

words = s.split()

for w in words:
    if len(w) > 900:
        print(len(w), w)
