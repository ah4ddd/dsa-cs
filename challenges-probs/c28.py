# Challenge 28 ~ Encode and Decode Strings

words = ["hello", "world", "python"]

def encode(words):
    encoded = ""

    for w in words:
        encoded += str(len(w))
        encoded += "#"
        encoded += w

    return encoded

def decode(encoded):
    decoded = []
    i = 0

    while i < len(encoded):
        j = i

        while encoded[j] != "#":
            j += 1

        length = int(encoded[i:j])

        word = encoded[j + 1 : j + 1 + length]
        decoded.append(word)

        i = j + 1  + length

    return decoded


encoded = encode(words)
print(encoded)

decoded = decode(encoded)
print(decoded)
