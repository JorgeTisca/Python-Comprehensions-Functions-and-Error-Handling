import random

dict = {}
for i in range(1, 5):
    dict[i] = i * 2

print("create dictionary with for -----", dict)

dict_v2 = {i: i * 2 for i in range(1, 5)}
print("create dictionary with dictionary Comprehension -----", dict)
print("-" * 20, "Create Dictionary with list and for", "-" * 20)

countries = ["col", "mex", "bol", "pe"]
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print("Create Dictionary with list and for-----", population)


print("-" * 20, "Create Dictionary Comprehension", "-" * 20)
population_v2 = {country: random.randint(1, 100) for country in countries}

print("Create Dictionary Comprehension-----", population)

print("-" * 20, "Create Dictionary using 2 lists", "-" * 20)
names = ["nico", "zule", "santi"]
ages = [12, 56, 98]

print("Combine lists names and age-----", list(zip(names, ages)))  # combine lists

new_dict = {name: age for (name, age) in zip(names, ages)}
print("Create Dictuinary comprehension using zip and 2 list---", new_dict)

names = ["nico", "zule", "santi"]
edades = [12, 56, 98]
new_dict = {names[i]: edades[i] for i in range(len(names))}

print("Create Dictionary other form using len---", new_dict)
