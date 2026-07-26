# Challenge 10 — First Unique Word

words = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "grape",
    "orange",
    "kiwi"
]

def get_first_unique_word(words):
    count = {}
    unique = []
    for w in words:
        if w in count:
            count[w] += 1
        else:
            count[w] = 1

    for c in count:
        if count[c] == 1:
            unique.append(c)

    if unique:
        return unique[0]

    return None


result = get_first_unique_word(words)

print(f"unique word: {result}")
