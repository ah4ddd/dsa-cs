# Challenge 30 -- Roman to Integer
# pattern is: Linear Traversal + Look Ahead (Look one step into the future.)

# Walk through a sequence once. Compare each element with its neighbor.
# If the next element is bigger, treat the current one as negative.
# Otherwise, treat it as positive. Sum everything

s = "MCMIV"

def roman_to_int(s):
    roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
    }

    total = 0

    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]

    return total

r = roman_to_int(s)

print(r)

