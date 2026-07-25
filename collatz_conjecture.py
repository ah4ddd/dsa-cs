x = 7

for _ in range(7):
    if x % 2 == 0:
        x = x // 2
    else:
        x = x * 3 + 1

    print(x)

"""
The rule:
    if even:
    divide by 2
else:
    multiply by 3 and add 1
"""

"""
Iterations:

First:
x = 7
not even
run else:
now x = 22
print(22)

second:
x = 22
is even:
now x = 11
print(11)

third:
x = 11
not even
run else:
now x = 34
print(34)

fourth:
x = 34
is even:
now x = 17
print(17)

fifth:
x = 17
not even
run else:
now x = 52
print(52)

sixth:
x = 52
is even:
now x = 26
print(26)

seventh
x = 26
is even:
now x = 13
print(13)
"""
