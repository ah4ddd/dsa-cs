nums=[2, 5, 7, 9, 13, 18, 22, 30, 45, 60, 78, 85, 100]

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

result = binary_search(nums, 85)
print("\nReturned Index:", result)

