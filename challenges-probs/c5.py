def get_largest(nums):
    if not nums:
        return None

    largest = nums[0]

    for n in nums[1:]:
        if n > largest:
            largest = n

    print(f"Largest: {largest}")

numbers = [-12, -7, -3, -25]

get_largest(numbers)
