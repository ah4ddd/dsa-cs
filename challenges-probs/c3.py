a = 1
b = 2

for _ in range(6):
    if a < b:
        a = a + b
    else:
        b = a - b

    print(a, b)

"""
Iterations:
3 2

3 1

3 2

3 1

3 2

3 1
"""
