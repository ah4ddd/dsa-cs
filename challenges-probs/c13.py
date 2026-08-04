# Challenge 13 — Two Sum

# solution 1 O(n²)
numbers = [2, 7, 11, 15]
target = 18

def two_sum(nums, target):

    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return i, j

    return None

result = two_sum(numbers, target)

print(f"sum: {result}")


# soluton 2 O(n)
def two_sum_two(nums, target):
    seen = {}
    for i, num in enumerate(nums):

        needed = target - num

        if needed in seen:
            return seen[needed], i

        seen[num] = i

    return None

result = two_sum_two(numbers, 17)

print(f"sum: {result}")


# Revisiting Challenge 13
nums = [5,1,9,8]
target = 13

def two_sums(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j

    return None

r = two_sums(nums, target)

print(r)
