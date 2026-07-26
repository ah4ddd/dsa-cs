# Challenge 12 — Is the List Sorted?

sorted_numbers = [3, 7, 12, 18, 25, 41]

unsorted_numbers = [3, 7, 18, 12, 25, 41]

def is_sorted(nums):
    n = len(nums)-1
    for i in range(n): # index-based traversal.
        if nums[i] > nums[i+1]:
            return False
    return True


result1 = is_sorted(sorted_numbers)
result2 = is_sorted(unsorted_numbers)

print(result1)
print(result2)
