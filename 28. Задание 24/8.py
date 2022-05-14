s = open("Файлы/8.txt").read()

# s = s.replace("XX", "X X")
# s = s.replace("XX", "X X")
# s = s.replace("YY", "Y Y")
# s = s.replace("YY", "Y Y")
# s = s.replace("ZZ", "Z Z")
# s = s.replace("ZZ", "Z Z")

for c in "XYZ":
    s = s.replace(2 * c, f"{c} {c}")
    s = s.replace(2 * c, f"{c} {c}")

for w in s.split():
    if len(w) > 25:
        print(len(w), w)
