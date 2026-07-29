# Challenge 22 — Two Sum (Brute Force)
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
