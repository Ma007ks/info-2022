from itertools import groupby

rows = [tuple(int(v) for v in line.split()) for line in open("26.txt")]

even_rows = sorted({row for row in rows if row[1] % 2 == 0})

for row, elements in groupby(even_rows, key=lambda row: row[0]):
    elements = list(elements)
    if len(elements) > 16:
        print(row, len(elements), elements)
