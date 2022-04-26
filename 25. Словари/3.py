from collections import Counter

with open("poem.txt", encoding="utf8") as file:
    sentence = file.read()

words = sentence.split()
words = [word.lower().rstrip(".,!?;…:") for word in words]
words = [word for word in words if word.isalpha()]

counts = Counter(words)

print(counts.most_common(5))

for word, count in counts.most_common():
    print(word, count)
