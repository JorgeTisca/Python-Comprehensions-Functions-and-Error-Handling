set_countries = {"col", "mex", "bol"}
# len() : Returns the size of the set
size = len(set_countries)
print("size of set_countries--", size)

print("exist 'col' in set_countries--", "col" in set_countries)
print("exist 'pe' in set_countries--", "pe" in set_countries)

print("-" * 20)

# add
set_countries.add("pe")
print("add 'pe--'", set_countries)
set_countries.add("pe")
print("try add 'pe' again--", set_countries)
print("-" * 20)

# update
set_countries.update({"ar", "ecua", "pe"})
print("update values 'ar', 'ecua' and try 'pe' again--", set_countries)

print("-" * 20)

# remove
set_countries.remove("col")
print("remove 'col'--", set_countries)

print("-" * 20)

# show error when dont exist value
try:
    set_countries.remove("arg")
    print(set_countries)

except Exception:
    print('Try remove "arg"-- value "arg" dont exist')

print("-" * 20)

# discard
set_countries.discard("arg")
print(
    "remove 'arg' using discard (remember this value dont exist in set_countries)--",
    set_countries,
)
print("-" * 20)

# clear
set_countries.clear()
print("Using clear--", set_countries)
