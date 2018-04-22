price = {
    "banana" :4,
    "apple" : 2,
    "orange": 1.5,
    "pear": 3,
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

for key,price_value in price.items():
    for stock_value in stock.values():
        message= '''        {0}
        price: {1}
        stock: {2}'''.format(key, price_value, stock_value)
        print(message, end="\n")
        print()

total =0
for price_value in price.values():
    for stock_value in stock.values():
        add_sum= price_value * stock_value
    print(add_sum)
    total += add_sum
print(total)
