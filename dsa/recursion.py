# Every recursive function must know when to stop.
# This stopping point is called the Base Case
# Without a base case, the function never ends.

def count(n):
    if n == 6:
        return

    print(n)

    count(n+1)

count(1)


print()


def countdown(n):

    # BASE CASE
    if n == 0:
        return

    print(n)

    # RECURSIVE CASE
    countdown(n - 1)

# The function has reached the end of its code,
# so Python removes it from the call stack and returns to the previous function.
