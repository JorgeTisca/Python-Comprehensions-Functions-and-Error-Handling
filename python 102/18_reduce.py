import functools

numbers = [1, 2, 3, 4]

result = functools.reduce(lambda counter, item: counter + item, numbers)

print("numbers--", numbers)
print("result counter numbers with reduce and lambda--", result, "\n")

print("use- function with reduce")


def accum(counter, item):
    print("counter--", counter)
    print("item--", item)
    print(f"{counter} + {item} = {counter+item}")
    return counter + item


result = functools.reduce(accum, numbers)

print(result)
