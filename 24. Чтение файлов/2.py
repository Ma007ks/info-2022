# str.split(sep) — нарезаем строчку на список строк (sep по умолчанию whitespace (\n, \t, пробел))
# str.splitlines() — нарезаем строчку на список строк (sep автоматически указан \n)

lines = open("2.txt").read().splitlines()

max_count_x = 0
max_line = None

for line in lines:
    curr_count_x = line.count("x")
    if curr_count_x > max_count_x:
        max_count_x = curr_count_x
        max_line = line

print(max_line)
print(max_count_x)


def get_count_x(line):
    return line.count("x")


print(max(lines, key=lambda line: line.count("x")))
print(max(lines, key=get_count_x))
