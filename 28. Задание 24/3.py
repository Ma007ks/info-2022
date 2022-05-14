s = open("Файлы/3.txt").read()

s = s.replace("ZY", "Z Y")
s = s.replace("ZX", "Z X")
s = s.replace("YX", "Y X")

words = s.split()

# print(max(len(w) for w in words))
# print(max(map(len, words)))
# print(w := max(words, key=len), len(w))

for w in words:
    if len(w) > 13:
        print(len(w), w)
