numbers = [1, 2, 3, 4, 5, 6]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Origin numbers--", numbers)
print("filter pair numbers-", new_numbers, "\n")


def filter_by_length(words):
    result = list(filter(lambda item: len(item) >= 4, words))
    return result


words = ["love", "sun", "rock", "day"]

print(words)
response = filter_by_length(words)
print("words with 4 or more letters--", response)
