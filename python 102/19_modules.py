import sys

print("-" * 20, "Import sys", "-" * 20)

print(sys.path, "\n")

print("-" * 20, "Import re", "-" * 20)
import re  # regular expresion

text = "My cellphone number is 449 34 79 54, code of State is 52, my luck number is 25"
result = re.findall("[0-9]+", text)  # find numbers
print("Find numbers with import re", result, "\n")

print("-" * 20, "Import time", "-" * 20)
import time

timetamp = time.time()
print("compute time--", timetamp)

local = time.localtime()
print("local time--", local)
result = time.asctime(local)
print("time--", result, "\n")

print("-" * 20, "Import collections", "-" * 20)
import collections

numbers = [1, 1, 2, 1, 2, 1, 4, 5, 3, 3, 21]
print(numbers)
counter = collections.Counter(numbers)
print("Dictionary with frequency of numbers", counter)
