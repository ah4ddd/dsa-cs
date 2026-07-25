x = 10

for _ in range(12):
    if x % 3 == 0:
        x = x - 4
    else:
        x = x + 5

    print(x)

"""
Iterations:
15

11

16

21

17

22

27

23

28

33

29

34
"""
