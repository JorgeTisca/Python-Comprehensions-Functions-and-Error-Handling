numbers = [1, 2, 3, 4]

numbers_v2 = []
for i in numbers:
    numbers_v2.append(i * 2)

print(numbers)
print(numbers_v2)

print("\n", "-" * 20, "used Map ", "-" * 20)

numbers_v3 = map(lambda i: i * 2, numbers)
# just use 1 line in code for see the same result

print(numbers)
print(list(numbers_v3))

print("\n", "-" * 20, "used Map with 2 list ", "-" * 20)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]
print(numbers_1)
print(numbers_2)

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))

print("just take the result of the short list")
print(result)
