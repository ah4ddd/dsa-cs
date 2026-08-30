class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini = nums[0]
        maxi = nums[0]

        minii = 0
        maxii = 0

        for i in range(len(nums)):
            if nums[i] > maxi:
                maxi = nums[i]
                maxii = i
            if nums[i] < mini:
                mini = nums[i]
                minii = i

        f = max(minii, maxii) + 1
        b = len(nums) - min(minii, maxii)

        s1 = maxii + 1 + (len(nums) - minii)
        s2 = minii + 1 + (len(nums) - maxii)

        return min(f, b, s1, s2)