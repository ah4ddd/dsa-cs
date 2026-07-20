# 1929. Concatenation of Array

# mine
class Solution:
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0]*(n*2)

        for i in range(n):
             ans[i] = nums[i]
             ans[i+n] = nums[i]

        return ans

sol = Solution()
array = [1, 2, 1, 2]

result = sol.getConcatenation(array)
print(result)


# neetcode
def concatenation(nums):
    ans = []
    for i in range(2):
        for n in nums:
            ans.append(n) # adds one object to the end of the list

    return ans

print(concatenation(array))

