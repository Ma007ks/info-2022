s = open("Файлы/4.txt").read()

# s = s.replace("A", " ")
# s = s.replace("B", " ")
# s = s.replace("C", " ")

s = s.replace("A", " ").replace("B", " ").replace("C", " ")

words = s.split()

print(max(map(len, words)))
