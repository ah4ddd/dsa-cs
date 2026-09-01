class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        seen = sorted(set(nums), reverse=True)

        if len(seen) >= 3:
            return seen[2]
        else:
            return seen[0]