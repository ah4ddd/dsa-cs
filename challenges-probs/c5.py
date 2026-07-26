numbers = [12, 7, 25, 3, 41, 18, 29]

def get_largest(nums):
    largest = 0

    for n in nums:
        if n > largest:
            largest = n

    print(f"Largest: {largest}")

get_largest(numbers)
