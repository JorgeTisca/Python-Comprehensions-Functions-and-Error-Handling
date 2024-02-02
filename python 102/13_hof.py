def increment(x):
    return x + 1


def hof(x, func):
    return x + func(x)


result = hof(2, increment)
# 2+(2+1)

print('use Higher order function "HOF" 2+(func(2)) ---', result)
print("-" * 20, "Transform function to lambda with hof", "-" * 20)

increment_v2 = lambda x: x + 1

hof_v2 = lambda x, func: x + func(x)
result = hof_v2(2, increment_v2)
print('use Higher order function "HOF" with lambda 2+(func(2)) ---', result)

result = hof_v2(2, lambda x: x + 2)  # you can use function if you undefined
print('use Higher order function "HOF" in result with lambda undefinded ---', result)

result = hof_v2(2, lambda arguments: arguments * 5)
print('use Higher order function "HOF" with lambda *5) ---', result)
