# prices[0] = 25
# prices[1] = 50
# prices[2] = 75
# prices[3] = 1000000

# products[0] = "гречка"
# products[1] = "рис"
# products[2] = "картофель"
# products[3] = "машина"

# key (ключ, аналог индекс) и value (значение)
# item = (key, value)

# prices["гречка"] = 25
# prices["рис"] = 50
# prices["картофель"] = 75
# prices["машина"] = 1000000

product_prices = {
    "гречка": 25,
    "рис": 50,
    "картофель": 75,
    "машина": 1000000,
}

print(len(product_prices))
# print(prices["гречка"])
# print(prices["машина"])

product_prices["пшено"] = 100

for product in product_prices:
    price = product_prices[product]
    print(f"{product} стоит {price}")

for product, price in product_prices.items():
    print(f"{product} стоит {price}")

print(product_prices.keys())
print(product_prices.values())
print(product_prices.items())

# total_price = sum(product_prices[product] for product in product_prices)
total_price = sum(product_prices.values())
print(total_price)
