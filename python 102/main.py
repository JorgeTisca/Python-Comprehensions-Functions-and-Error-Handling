import pkg.mod_2 as mod_2
import pkg.mod_3 as mod_3
from pkg.mod_1 import func_1, func_2

print("-" * 20, "Import function of mod 1", "-" * 20)
print(func_1())
print(func_2())

print("-" * 20, "Import function of mod 2 with as", "-" * 20)
print(mod_2.func_3())
print(mod_2.func_4())

print("-" * 20, "Import function of mod 3 with . ", "-" * 20)
print(mod_3.func_5())
print(mod_3.func_6())
