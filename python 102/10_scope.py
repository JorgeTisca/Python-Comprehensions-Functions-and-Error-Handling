prince = 100  # global


def scope():
    prince = 200  # function
    prince += 10
    return prince


print("value global--", prince)  # global
prince_2 = scope()
print("function value--", prince_2)  # function
