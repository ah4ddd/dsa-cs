# Challenge 11 — Linear Search

numbers = [12, 7, 25, 3, 41, 18, 29]

def linear_search(nums, target):
    for i, n in enumerate(nums):
        if n == target:
            return i

    return None

result = linear_search(numbers, 41)

print(f"Your integer index: {result}")
