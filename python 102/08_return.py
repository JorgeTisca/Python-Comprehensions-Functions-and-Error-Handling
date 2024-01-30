def sum_with_range(min, max):
    sum = 0
    for x in range(min, max):
        sum += x
    print(f"sum between {min} to  {max} =", sum)


sum_with_range(1, 10)
sum_with_range(20, 30)

print("-" * 20, "use return", "-" * 20)


def sum_with_range_return(min, max):
    print(f"sum between {min} to  {max} =")
    sum = 0
    for x in range(min, max):
        sum += x
    return sum


result = sum_with_range_return(1, 20)
print(result)

result_2 = sum_with_range_return(result, result + 10)
print(result_2)
