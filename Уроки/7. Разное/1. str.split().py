# str.split() возвращает список строк!

s = "53; 14; 12"

a, b, c = s.split("; ")

a = int(a)
b = int(b)
c = int(c)

print(a + b + c)
