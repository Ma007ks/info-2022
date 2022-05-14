s = open("Файлы/13.txt").read()

# s = s.replace("00", "0 0")
# s = s.replace("11", "1 1")
# s = s.replace("22", "2 2")
# s = s.replace("33", "3 3")
# s = s.replace("44", "4 4")
# s = s.replace("55", "5 5")
# s = s.replace("66", "6 6")
# s = s.replace("77", "7 7")
# s = s.replace("88", "8 8")
# s = s.replace("99", "9 9")

for d in "0123456789":
    s = s.replace(d + d, d + " " + d)

for w in s.split():
    if len(w) >= 100:
        print(len(w), w)
