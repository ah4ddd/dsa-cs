numbers = [12, 7, 25, 3, 41, 18, 29]

def get_smallest(nums):
    smallest = nums[0]

    for n in nums[1:]:
        if n < smallest:
            smallest = n

    print(f" smallest number in array: {smallest}")

get_smallest(numbers)

