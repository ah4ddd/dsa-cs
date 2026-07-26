def fibonacci(n):
    a = 0
    b = 1

    for _ in range(n):
        print(a)

        temp = a + b
        a = b
        b = temp

fibonacci(11)

"""
iterations:
first:
a = 0
b = 1
p = 0

second:
a = 1
b = 1
p = 1

third:
a = 1
b = 2
p = 1

fourth:
a = 2
b = 3
p = 2

fifth:
a = 3
b = 5
p = 3

sixth:
a = 5
b = 8
p = 5

seventh:
a = 8
b = 13
p = 8

eight:
a = 13
b = 21
p = 13

ninth:
a = 21
b = 34
p = 21

tenth:
a = 34
b = 55
p = 34

a = current Fibonacci number
b = next Fibonacci number
"""
