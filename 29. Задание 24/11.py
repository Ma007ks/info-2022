from collections import Counter

s = open("11.txt").read()

counter = Counter(s[i + 1] for i in range(len(s) - 1) if s[i] == "A")

print(counter.most_common())
