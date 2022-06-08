# n, *nums = [int(line) for line in open("27-a.txt")]
from random import randrange

n, *weights = map(int, open("27-b.txt"))
min_total_price = float("inf")

while True:
    station = randrange(206940 - 20, 206940 + 20)

    # Общая стоимость перевозки, если пункт переработки имеет номер station
    total_price = 0

    for i in range(n):
        distance = abs(station - i)
        price = min(distance, n - distance) * weights[i]
        total_price += price

    if total_price < min_total_price:
        min_total_price = total_price
