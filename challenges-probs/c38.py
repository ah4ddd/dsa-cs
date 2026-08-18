# 3471. Find the Largest Almost Missing Integer

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        # number → how many k-sized windows contain that number
        count = {}

        # Look at every subarray (window) of size k
        for start in range(len(nums) - k + 1):

            window = nums[start:start + k]

            # A number should be counted only once per window
            for n in set(window):
                if n in count:
                    count[n] += 1
                else:
                    count[n] = 1

        # Find the largest number that appears in exactly one window
        answer = -1

        for n in count:
            if count[n] == 1:
                if n > answer:
                    answer = n

        return answer


obj = Solution()
r = obj.largestInteger(nums=[3,9,2,1,7,10], k=3)
print(r)

