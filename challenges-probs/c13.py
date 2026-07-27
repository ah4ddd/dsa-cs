# Challenge 13 — Two Sum

numbers = [2, 7, 11, 15]
target = 17

def two_sum(nums, target):
    n = len(nums)-1
    for i in range(n):
        if nums[i] + nums[i+1] == target:
            return i, i+1

    return None

result = two_sum(numbers, target)

print(f"sum: {result}")
