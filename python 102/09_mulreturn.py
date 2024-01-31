def find_volume(length=1, width=2, depth=3):
    return length * width * depth, width, "hello"
    # return [ length * width * depth, width, "hello"]    #get list


result = find_volume(width=10)

print("multiple return values--", result)

print("return specific position--", result[1])

result, width, text = find_volume(width=10)

print("return specific text--", text)
