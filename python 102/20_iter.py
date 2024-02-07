print("-" * 20, "Iteration with For", "-" * 20)
for i in range(1, 10):
    print(i)

print("-" * 20, "Iteration with iter", "-" * 20)

my_iter = iter(range(1, 4))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

fruit = ("apple", "orange", "banana")
myit = iter(fruit)

print(next(myit))
print(next(myit))
print(next(myit))
