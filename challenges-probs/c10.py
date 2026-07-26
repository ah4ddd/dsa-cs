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
    for w in words:
        if w in count:
            count[w] += 1
        else:
            count[w] = 1

    for w in words:
        if count[w] == 1:
            return w

    return None


result = get_first_unique_word(words)
print(f"unique word: {result}")
