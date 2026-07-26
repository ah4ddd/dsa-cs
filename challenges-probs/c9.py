# Challenge 9 — Count Duplicates

words = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple",
    "grape",
]

def count_duplicates(words):
    duplicates = {}

    for w in words:
        if w in duplicates:
            duplicates[w] += 1
        else:
            duplicates[w] = 1

    return duplicates

print(count_duplicates(words))
