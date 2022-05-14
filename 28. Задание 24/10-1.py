s = open("Файлы/10.txt").read()

s = s.replace("AB", "X")
s = s.replace("CB", "Y")

s = s.replace("A", " ")
s = s.replace("B", " ")
s = s.replace("C", " ")

for w in s.split():
    if len(w) >= 60:
        print(len(w), w)
