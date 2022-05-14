s = open("Файлы/2.txt").read()

print(s[:100])

s = s.replace("Z", "разрез")

words = s.split()

print(s[:100])
# print(words[:15])
#
# print(max(len(w) for w in words))
