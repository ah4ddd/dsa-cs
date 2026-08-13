# C33 -- Merge Sorted Array

# SOL !
def mergesort(nums1, m, nums2, n):
    nums1[:] = sorted(nums1[:m] + nums2)

    return nums1

r = mergesort(nums1=[1,2,3,4,0,0,0], m=4, nums2=[2,4,5,6,7,8], n=6)

print(r)



# SOL 2 (Two Pointers)
def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # Moved OUTSIDE the while loop so it runs after the loop completely finishes
    return nums1

# FIXED: nums1 now has 10 total slots to fit m (4) + n (6) elements
nums1 = [1, 2, 3, 4, 0, 0, 0, 0, 0, 0]
nums2 = [2, 4, 5, 6, 7, 8]

rs = merge(nums1=nums1, m=4, nums2=nums2, n=6)
print(rs)

# Binary Search (Two pointers example)

def binary_search(arr, target):
    # Here are your two pointers forming the boundaries
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Found it!

        elif arr[mid] < target:
            left = mid + 1   # Move the left pointer forward
        else:
            right = mid - 1  # Move the right pointer backward

    return -1  # Target doesn't exist
