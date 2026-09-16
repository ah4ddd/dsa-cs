class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maximum = 0
        
        for n in nums:
            if n == 1:
                count += 1
                maximum = max(maximum, count)
            else:
                count = 0
        return maximum