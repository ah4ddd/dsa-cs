# C33 -- Merge Sorted Array

# SOL !
def mergesort(nums1, m, nums2, n):
    nums1[:] = sorted(nums1[:m] + nums2)

    return nums1

r = mergesort(nums1=[1,2,3,4,0,0,0,0,0,0], m=4, nums2=[2,4,5,6,7,8], n=6)

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
nums1 = [1,2,3,0,0,0],
nums2 = [2,5,6]

rs = merge(nums1=nums1, m=3, nums2=nums2, n=3)
print(rs)



# Binary Search (Two pointers example)
# Have two index variables
# and move them around while processing the arrays.
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # 1. Initialize your two boundary pointers
        left = 0
        right = len(nums) - 1

        # 2. Squeeze the search zone from both ends
        while left <= right:
            # Find the middle index between the two pointers
            mid = (left + right) // 2

            # Case A: You guessed it perfectly
            if nums[mid] == target:
                return mid

            # Case B: The middle number is too small, discard the left half
            elif nums[mid] < target:
                left = mid + 1   # Move left pointer past mid

            # Case C: The middle number is too big, discard the right half
            else:
                right = mid - 1  # Move right pointer below mid

        # 3. If pointers cross and we find nothing, the target isn't there
        return -1


# ==========================================
# LOCAL TEST BLOCK (Run this file directly)
# ==========================================
if __name__ == "__main__":
    sol = Solution()

    # Sorted array input
    test_nums = [-1, 0, 3, 5, 9, 12]
    test_target = 9

    # Execute the search
    result_index = sol.search(test_nums, test_target)

    print("--- RUNNING BINARY SEARCH ---")
    print(f"Input Array: {test_nums}")
    print(f"Target Value: {test_target}")
    print(f"Target found at Index: {result_index}")  # Should output 4

