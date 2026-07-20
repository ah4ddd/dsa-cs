class Solution:
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0]*(2*n)

        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]

        return ans

sol = Solution()
array = [1, 2, 1]

result = sol.getConcatenation(array)
print(result)


