def get_fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
        # next number = a + b (could use)
        # a = b
        # b = next_number
    return a

user_input = input("Which Fibonacci number do you want to find? ")

target_number = int(user_input)

answer = get_fibonacci(target_number)
print(f"The {target_number}th Fibonacci number is: {answer}")

"""
Iterations(10)

a=0
b=1

a=1
b=1

a=1
b=2

a=2
b=3

a=3
b=5

a=5
b=8

a=8
b=13

a=13
b=21

a=21
b=34

a=34
b=55
"""
