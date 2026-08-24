class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        l = max(nums)
        li = nums.index(l)

        for n in nums:
            if n != l and l < n*2:
                return -1

        return li

        
            