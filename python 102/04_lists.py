numbers = []
for i in range(1, 11):
    numbers.append(i)

print("create list with for -----", numbers)

numbers_v2 = [element for element in range(1, 11)]
print("create list with list comprehension-----", numbers_v2)
numbers = []

print("-" * 15, "elements x 2", "-" * 15)
for element in range(1, 11):
    numbers.append(element * 2)

print("create list with for -----", numbers)

numbers_v2 = [element * 2 for element in range(1, 11)]
print("create list with list comprehension-----", numbers_v2)


print("-" * 20, "List comprehension with conditional", "-" * 20)

print("-" * 20, "Example simple with cycles and conditionals", "-" * 20)

numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i)
print("just print pair numbers of 1 to 10--->", numbers)

print("-" * 20, "Example List comprehension with conditional", "-" * 20)
