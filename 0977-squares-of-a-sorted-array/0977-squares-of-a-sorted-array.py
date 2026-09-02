class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        
        result = [0]*len(nums)
        p = len(nums)-1
        
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result[p] = nums[l]**2
                l += 1
            else:
                result[p] = nums[r]**2
                r -= 1

            p -= 1
        
        return result