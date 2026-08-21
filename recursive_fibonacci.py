def fibonacci(n):

    # ------------------------
    # BASE CASES
    # ------------------------

    if n == 0:
        return 0

    if n == 1:
        return 1

    # ------------------------
    # RECURSIVE CASE
    # ------------------------

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
