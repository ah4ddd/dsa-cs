class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        un = set(nums)
        ls = 0

        for n in un:
            if n-1 not in un:
                l = 1

                while n + l in un:
                    l += 1
                
                ls = max(l, ls)

        return ls

