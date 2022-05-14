s = open("Файлы/10.txt").read()

s = s.replace("AA", "A A")
s = s.replace("AA", "A A")
s = s.replace("BB", "B B")
s = s.replace("BB", "B B")
s = s.replace("CC", "C C")
s = s.replace("CC", "C C")

s = s.replace("AC", "A C")
s = s.replace("CA", "C A")

for w in s.split():
    if len(w) >= 120:
        print(len(w), w)
