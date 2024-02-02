def increment(x):
    return x + 1


result = increment(10)
print("result increment---", result)

print("-" * 30, "Transoform function to lambda", "-" * 30)
increment_v2 = lambda x: x + 1

result = increment_v2(20)
print("result increment v2---", result)

print("\t")
full_name = lambda name, last_name: f"Full name is {name.title()} {last_name.title()}"

text = full_name("jorge", "tisca")
print("use lambda with more arguments---", text)
