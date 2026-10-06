class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, n in enumerate(nums):
            needed = target - n

            if needed in seen:
                return seen[needed], i
            
            seen[n] = i
        