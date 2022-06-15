from collections import Counter, defaultdict

rows = [tuple(int(v) for v in line.split()) for line in open("26.txt")]

even_rows = {row for row in rows if row[1] % 2 == 0}

counter = Counter(row[0] for row in even_rows)
# counts = {}
counts = defaultdict(int)

for row, column in even_rows:
    # if row not in counts:
    #     counts[row] = 0
    counts[row] += 1

print(counts)
# print(counter.most_common(5))
