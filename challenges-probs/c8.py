# Challenge 8 — Find Both Smallest and Largest

numbers = [12, 7, 25, 3, 41, 18, 29]

def get_large_small(nums):
    largest = nums[0]
    smallest = nums[0]

    for n in nums:
        if n < smallest:
            smallest = n
        elif n > largest:
            largest = n

    return largest, smallest


largest, smallest = get_large_small(numbers)

print(f"Smallest: {smallest}, Largest: {largest}")
