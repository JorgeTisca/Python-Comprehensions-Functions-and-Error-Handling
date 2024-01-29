set_a = {"col", "mex", "bol"}
set_b = {"pe", "bol"}

print("-" * 10, "Union", "-" * 10)
# Union
print(set_a, "Union or |", set_b)
set_c = set_a.union(set_b)
print("Use Union in set a and set b---", set_c)
set_c = set_a | set_b
print('Use "|" (Union) in set a and set b---', set_c)

print("-" * 10, "Intersection", "-" * 10)
# Intersection
print(set_a, "intersection or &", set_b)
set_c = set_a.intersection(set_b)
print("Show the equals elements in sets with intersection---", set_c)
set_c = set_a & set_b
print("Show the equals elements in sets with '&'---", set_c)

print("-" * 10, "Difference", "-" * 10)
# Difference is the rest of elements
print(set_a, "difference or - ", set_b)
set_c = set_a.difference(set_b)
print(set_c)
set_c = set_a - set_b
print(set_c)

print("-" * 10, "Symetric Difference", "-" * 10)
print(set_a, "Symetric difference or ^ ", set_b)
# Symetric Difference delete equals values
set_c = set_a.symmetric_difference(set_b)
print("Delete equals values with symmetric difference--", set_c)
set_c = set_a ^ set_b
print("Delete equals values with ^ --", set_c)
