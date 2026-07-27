# Challenge 17 — Find the First Non-Repeating Number

numbers1 = [4, 2, 1, 2, 1, 7, 4]

numbers2 = [5, 3, 5, 2, 2, 9]

numbers3 = [1, 1, 2, 2]

def first_unique(nums):
    count = {}

    for n in nums:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    for c in count:
        if count[c] == 1:
            return c

    return None

result1 = first_unique(numbers1)
print(result1)

result2 = first_unique(numbers2)
print(result2)

result3 = first_unique(numbers3)
print(result3)
