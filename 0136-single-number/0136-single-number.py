class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}

        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1

        for k, v in seen.items():
            if v == 1:
                return k
            
        