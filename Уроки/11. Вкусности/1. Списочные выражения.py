# [1, 4, 9, 16, 25, ..., 400]
# list comprehension

# statements — инструкции
# expressions — выражения

squares = []
for x in range(1, 21):
    squares.append(x ** 2)

# [выражение for переменная in коллекция]

new_squares = [x ** 2 for x in range(1, 21)]

print(squares)
print(new_squares)
