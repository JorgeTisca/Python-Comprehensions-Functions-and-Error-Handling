try:
    print(0 / 0)
except Exception as error:
    print(error)

try:
    assert 1 != 1, "Error Error Error Error"
except Exception as error:
    print(error)

print("Hello")


def my_divide(a, b):

    try:
        result = a / b
    except Exception as error:
        result = "No se puede dividir por 0"
    return result


response = my_divide(10, 2)
print(response)

response = my_divide(10, 0)
print(response)
