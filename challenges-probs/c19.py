# Challenge 19 — Majority Element
# returns the number that appears more than half of the total length of the list.

numbers = [3, 2, 3]

numbers2 = [2, 2, 1, 1, 1, 2, 2]

numbers3 = [7, 7, 7, 4, 5]

numbers4 = [8, 4, 8, 2, 8, 3, 8, 1, 8]

numbers5 = [1, 1, 1, 100]

numbers6 = [5, 5, 1, 1, 1]

def get_majority_element(nums):
    major = {}
    highest_value = float("-inf")
    major_key = 0

    for i in range(len(nums)):
        if nums[i] in major:
            major[nums[i]] += 1
        else:
            major[nums[i]] = 1

    for key, value in major.items():
        if value > highest_value:
            highest_value = value
            major_key = key

    print(major)

    return major_key

result = get_majority_element(numbers6)

print(result)
