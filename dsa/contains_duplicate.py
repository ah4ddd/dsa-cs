# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

# Test Case 1 - Duplicate at the end
array1 = [1, 2, 3, 1]
# Expected: True

# Test Case 2 - All unique
array2 = [1, 2, 3, 4, 5]
# Expected: False

# Test Case 3 - Many duplicates
array3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Expected: True

# Test Case 4 - Duplicate in the middle
array4 = [10, 20, 30, 40, 20, 50]
# Expected: True

sol = Solution()

print(sol.containsDuplicate(array1))  # True
print(sol.containsDuplicate(array2))  # False
print(sol.containsDuplicate(array3))  # True
print(sol.containsDuplicate(array4))  # True


"""
We create an empty set called seen to keep track of numbers we've already encountered.
Then we iterate through the array one element at a time. For each number,
we first check whether it already exists in seen. If it does, we've found a duplicate,
so we immediately return True. If it doesn't, we add it to seen and continue.
If we finish iterating through the entire array without finding any duplicates, we return False.
"""
