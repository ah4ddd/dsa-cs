class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t = sum(nums)
        l = 0
        
        for i, n in enumerate(nums):
            if l == (t - l - n):
                return i
            l += n
            
        return -1