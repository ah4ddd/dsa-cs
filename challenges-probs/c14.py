# Challenge 14 — Find the Second Largest Number

numbers = [12, 65, 70, 7, 40, 75, 42, 8, 90, 98]

def get_second_largest(nums):
    largest = nums[0]
    second_largest = nums[0]

    for n in nums:
        if n > largest:
            second_largest = largest
            largest = n
        elif n > second_largest:
            second_largest = n

    if second_largest < largest:
        return second_largest
    return None

result = get_second_largest(numbers)
print(result)
