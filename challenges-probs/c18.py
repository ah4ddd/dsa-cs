# Challenge 18 — Find the Missing Number


numbers = [1, 2, 4, 5]
numbers = [1, 3, 4, 5]
numbers = [2, 3, 1, 5, 6, 7, 8, 10]


def get_missing_numbers(nums):
    missing = {}
    answer = []
    smallest = nums[0]
    largest = nums[0]


    for n in nums:
        missing[n] = 1
        if n < smallest:
            smallest = n
        elif n > largest:
            largest = n

    for i in range(smallest, largest+1):
        if i not in missing:
            answer.append(i)

    return answer


result = get_missing_numbers(numbers)

print(result)
