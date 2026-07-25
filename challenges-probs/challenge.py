# still fibonacci

a = 2
b = 3

for _ in range(5):
    print(a, b)

    temp = a + b
    a = b
    b = temp


"""
first:
a = 2
b = 3
print = 2 3

second:
a = 3
b = 5
print = 3 5

third:
a = 5
b = 8
print = 5 8

fourth:
a = 8
b = 13
print = 8 13

fifth:
a = 13
b = 21
print = 13 21
"""
