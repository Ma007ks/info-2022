s = open("Файлы/12.txt").read()

s = s.replace("000", "00 00")
s = s.replace("000", "00 00")
s = s.replace("000", "00 00")

for w in s.split():
    if len(w) > 7000:
        print(len(w), w)
