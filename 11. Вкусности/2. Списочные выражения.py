# [выражение for переменная in коллекция if условие]

# squares = []
# for x in range(1, 101):
#     if (x ** 2) % 10 == 9:
#         squares.append(x ** 2)
#
# new_squares = [x ** 2 for x in range(1, 101) if (x ** 2) % 10 == 9]
#
# print(squares)
# print(new_squares)

from random import randrange, seed

seed(4532)

numbers = [randrange(-9, 10) for _ in range(randrange(5, 25))]

# odds = []
# for number in numbers:
#     if number % 2 == 1:
#         odds.append(number)

odds = [n for n in numbers if n % 2]
even = [n for n in numbers if n % 2 == 0]
positive = [n for n in numbers if n > 0]
two_digit = [n for n in numbers if 10 <= abs(n) <= 99]
ends_with_3 = [n for n in numbers if n % 10 == 3]

print("Numbers:", numbers)
print("Odds:", odds)
print("Even:", even)
print("Positive:", positive)
print("Two digit:", two_digit)
print("Ends with 3:", ends_with_3)

# print(sum(two_digit))
# print(max(ends_with_3))
# print(min(ends_with_3))
# print(len(ends_with_3))

ends_with_3_set = {n for n in numbers if n % 2}

print(ends_with_3_set)

s = sum(n for n in numbers if n < 0)
mx = max(n for n in numbers if n < 0)
mn = min(n for n in numbers if n < 0)

print(s)
