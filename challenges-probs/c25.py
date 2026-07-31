# Challenge 25 — Longest Consecutive Sequence


nums = [100, 4, 200, 1, 3, 2]
nums = [1, 2, 3, 4, 5]
nums = [5, 4, 3, 2, 1]
nums = [10, 30, 50, 70]
nums = [1, 2, 2, 3, 4]
nums = [1, 1, 1, 2, 2, 3, 3, 4]
nums = [-3, -2, -1, 0, 1]
nums = [-2, 4, -1, 0, 1, 3, 2]
nums = [42]
nums = []
nums = [10, 11, 12, 50, 51]
nums = [8, 1, 6, 2, 10, 3, 5, 4, 9, 7]
nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
nums = [5, 5, 4, 3, 2, 1]
nums = [100, 101, 5, 6, 7, 8, 50]

def longest_consecutive(nums):
    lc = set(nums)
    count = 0

    for c in lc:

        if c - 1 in lc:
            count += 1
        elif c + 1 in lc:
            count += 1


    if count > 0:
        return count

    return 0


result = longest_consecutive(nums)
print(result)
