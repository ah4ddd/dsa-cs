class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        r = []
        t = 0

        for n in nums:
            t += n
            r.append(t)

        return r