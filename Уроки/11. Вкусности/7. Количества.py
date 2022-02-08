numbers = [15, 16, 4, 3, 5, 8, 10, 10, 4, 8, 20, 10, 1, 4, 11, 8, 17, 13, 13, 6]

count_even = 0
for n in numbers:
    if n % 2 == 0:
        count_even += 1

print(count_even)

evens = [n for n in numbers if n % 2 == 0]
print(len(evens))

sum_evens = sum(n for n in numbers if n % 2 == 0)
count_evens = sum(1 for n in numbers if n % 2 == 0)
count_evens_2 = sum(n % 2 == 0 for n in numbers)
count_ends_with_3 = sum(n % 10 == 3 for n in numbers)
count_more_10 = sum(n > 10 for n in numbers)
numbers_more_10 = [n for n in numbers if n > 10]

# print(sum_evens)
print(count_evens)
print(count_evens_2)

print([n % 2 == 0 for n in numbers])
print(count_ends_with_3)
print(count_more_10)
print(len(numbers_more_10))

count_more_10 = len(numbers_more_10 := [n for n in numbers if n > 10])

# from functools import reduce
#
#
# def mul(res, x):
#     return res * x
#
#
# print(reduce(mul, range(1, 6)))
# print(reduce(lambda res, x: res * x, range(1, 6)))
