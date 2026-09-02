class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ln = max(nums)
        li = nums.index(ln)
        
        for n in nums:
            if n != ln and ln < n*2:
                return -1
            
        return li