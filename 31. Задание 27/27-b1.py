n, *weights = map(int, open("27-b.txt"))

min_total_price = float("inf")

for station in range(206935, 206950, 1):
    total_price = 0

    for i in range(n):
        distance = abs(station - i)
        price = min(distance, n - distance) * weights[i]
        total_price += price

    if total_price < min_total_price:
        min_total_price = total_price
        print(">>>>", station, total_price)
