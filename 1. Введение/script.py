print(3 + 5)
print("Hello, world!", end=" :)")

print(2 ** 3)

print(1, 2, 3, 4, 5, sep="")
print(1, 2, 3, 4, 5, sep="*-*")  # некрасиво!
print("1, 2, 3, 4, 5")

# Переменная — это ссылка на какой-то объект

x = 2 ** 100

print(x)
print(1267650600228229401496703205376)
print(2 ** 100)
print(x * 5)
print(x)
print(type(x))

x = 'Hello'

print(x)
print(type(x))

a, b = 3, 7

print(a)
print(b)
print(a + b)

a = a + 3
a += 3
print(a)

b *= 2

print(b)

b **= 2

print(b)

b /= a

print(b)
