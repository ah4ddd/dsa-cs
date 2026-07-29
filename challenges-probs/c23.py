# CHALLENGE 23 — VALID PALINDROME
# Revisiting Challenge 16


def is_palindrome(text):
    for i in range(len(text) //2):
        if text[i] != text[-(i+1)]:
            return False

    return True


r = is_palindrome("racecar")
print(r)
