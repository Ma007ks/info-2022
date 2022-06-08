# n, *nums = [int(line) for line in open("27-a.txt")]
n, *weights = map(int, open("27-a.txt"))

for station in range(n):
    # Общая стоимость перевозки, если пункт переработки имеет номер station
    total_price = 0

    for i in range(n):
        distance = abs(station - i)
        price = min(distance, n - distance) * weights[i]
        total_price += price

    if total_price < 157242:
        print(total_price, station)
