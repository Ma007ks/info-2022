rows = [tuple(int(v) for v in line.split()) for line in open("26.txt")]
even_rows = {row for row in rows if row[1] % 2 == 0}

only_rows_numbers = [row[0] for row in even_rows]

for i in set(only_rows_numbers):
    count = only_rows_numbers.count(i)
    if count >= 17:
        print(i, count)
