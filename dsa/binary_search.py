def binary_search(nums, target):
# The variables left, right, and mid always store INDEXES, not the actual values from the array.
    left = 0
    right = len(nums) - 1

    print("Array :", nums)
    print("Target:", target)
    print()

    while left <= right:

        print("-----------------------------")
        print("left :", left)
        print("right:", right)

        print(f"Calculating mid = ({left} + {right}) // 2")
        mid = (left + right) // 2

        print("mid  :", mid)
        print("Value at mid:", nums[mid]) # 9

        if nums[mid] == target:
            print("Target Found!")
            return mid

        elif nums[mid] < target:
            print("Target is BIGGER.")
            print("Move left pointer.")

            left = mid + 1

        else:
            print("Target is SMALLER.")
            print("Move right pointer.")

            right = mid - 1

    print("Target not found.")
    # return the integer -1 as a special 'not found' signal," not "return the element at index -1.
    return -1

nums = [2, 5, 7, 9, 13, 18, 22, 30]
result = binary_search(nums, 5)
print("\nReturned Index:", result)
