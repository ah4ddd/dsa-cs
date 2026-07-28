# Challenge 18 — Find the Missing Number


numbers = [1, 2, 4, 5]
numbers = [1, 3, 4, 5]
numbers = [2, 3, 1, 5]
numbers = [4, 1, 2, 5]

def get_missing_numbers(nums):
    missing = {}

    for n in nums:
        missing[n] = True

    for i in range(1, len(nums)+2):
        if i not in missing:
            return i

    return None


result = get_missing_numbers(numbers)

print(result)
