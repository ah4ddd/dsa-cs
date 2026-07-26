# Challenge 6 — Sum Only Even Numbers

numbers = [7, 12, 5, 18, 21, 30, 9, 4]

def sum_even(nums):
    even = []
    sum = 0
    for n in nums:
        if n % 2 == 0:
            sum += n
            even.append(n)

    print(f"sum of even numbers: {sum}")


sum_even(numbers)
