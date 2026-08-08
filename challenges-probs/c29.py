# Challenge 29 — Valid Parentheses

s = "()[]{}"

def is_valid(s):
    stack = []
    pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
    }

    for c in s:
        if c in "([{":
            stack.append(c)
        else:
            if len(stack) == 0:
                return False

            if stack[-1] != pairs[c]:
                return False

            stack.pop()

    return len(stack) == 0


result = is_valid(s)
print(result)
