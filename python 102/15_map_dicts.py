items = [
    {"product": "shirt", "price": 100},
    {"product": "jeans", "price": 300},
    {"product": "pants", "price": 200},
]
# show price of products
prices = list(map(lambda item: item["price"], items))
print("price of products in dictionary", prices)


# add item but modify the original map
# def add_taxes(item):
#     item["taxes"] = item["price"] * 0.19
#     return item


# add item but not modify the origin map
def add_taxes(item):
    items_copy = item.copy()
    items_copy["taxes"] = items_copy["price"] * 0.19
    return items_copy


new_items = list(map(add_taxes, items))
print("add taxes-", new_items)
print("Origin map--", items)

print("-" * 20, "Practice with MAP", "-" * 20)


# practice with map
def multiply_numbers(numbers):
    result = list(map(lambda number: number * 2, numbers))
    return result


numbers = [1, 2, 3, 4]
print("origin numbers---", numbers)
response = multiply_numbers(numbers)
print("numbers * 2 ", response)
