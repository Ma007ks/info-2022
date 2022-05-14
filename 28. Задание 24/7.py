s = open("Файлы/7.txt").read()

s = s.replace("12", "1 2")
s = s.replace("13", "1 3")
s = s.replace("31", "3 1")
s = s.replace("21", "2 1")


for w in s.split():
    if len(w) > 300:
        print(len(w), w)
