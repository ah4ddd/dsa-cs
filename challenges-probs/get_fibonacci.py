def get_fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

user_input = input("Which Fibonacci number do you want to find? ")

target_number = int(user_input)

answer = get_fibonacci(target_number)
print(f"The {target_number}th Fibonacci number is: {answer}")

