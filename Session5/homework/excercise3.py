price = {
    "banana" : 4,
    "apple" : 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for key, price_value in price.items():
    message= '''     {0}
        price: {1}
        stock: {2}'''.format(key, price[key], stock[key])
    print(message, end="\n")
    print()

total =0
for key,value in price.items():
    add_sum= price[key] * stock[key]
    print(add_sum)
    total+= add_sum
print("Total =", total)        
