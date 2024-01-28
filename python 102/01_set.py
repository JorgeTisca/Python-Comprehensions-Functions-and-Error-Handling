set_countries = {
    "col",
    "mex",
    "bol",
}
# Dont have key-value is different to directory
print("set String--", set_countries)
print(type(set_countries))

# Remove repeated values
set_numbers = {1, 2, 2, 443, 23}
print("set Numbers--", set_numbers)

# Can use different types values
set_types = {1, "hola", False, 12.12}
print("set difenrents vars--", set_types)

set_from_string = set("hello")
print("set from String--", set_from_string)

set_from_tuples = set(("abc", "cvb", "nmh", "abc"))
print("set from tuples--", set_from_tuples)

numbers = [1, 2, 3, 4, 1, 2, 5, 6]
set_numbers = set(numbers)
print("set from list--", set_numbers)

unique_numbers = list(set_numbers)
print("transform set to list--", set_numbers, "position 3 is ", unique_numbers[2])
