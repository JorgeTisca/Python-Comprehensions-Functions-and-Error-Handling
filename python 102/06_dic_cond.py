import random

countries = ["col", "mex", "bol", "pe"]

population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

result = {
    country: population
    for (country, population) in population_v2.items()
    if population > 20
}
print("result of conditional where population >20----", result)


print("-" * 20, "Used dictionary comprehension with Strings", "-" * 20)

text = "Hello, I am Jorge"
unique = {c: c.upper() for c in text if c in "aeiou"}
print(f"get vocals of text -->'{text} 'with dictionary comprehension---", unique)
