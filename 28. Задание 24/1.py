s = open("Файлы/1.txt").read()
words = s.split()

print(max(len(w) for w in words))

print(max(map(len, words)))

for w in words:
    if len(w) > 250:
        print(len(w), w)

word = max(words, key=len)
print(word)
print(len(word))
