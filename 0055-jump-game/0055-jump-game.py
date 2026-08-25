class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        # maximum position reachable so far
        furthest = 0

        for i in range(len(nums)):

            if i > furthest:
                return False

            furthest = max(furthest, i + nums[i])

            if furthest >= last:
                return True

        return False