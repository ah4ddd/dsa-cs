a = 3
b = 5

for _ in range(5):
    if a % 2 == 0:
        a = a + b
    else:
        b = b + a

    print(a, b)


"""
Iterations:

3 8

3 11

3 14

3 17

3 20
"""
