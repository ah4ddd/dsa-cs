numbers = [7, 12, 5, 18, 21, 30, 9, 4]

def get_even_odd(nums):
    even = []
    odd = []

    for n in nums:
        if n % 2 ==  0:
            even.append(n)
        else:
            odd.append(n)

    print(f"evens: {even}")
    print(f"total evens: {len(even)}")
    print(f"odds: {odd}")
    print(f"total odds: {len(odd)}")

get_even_odd(numbers)
