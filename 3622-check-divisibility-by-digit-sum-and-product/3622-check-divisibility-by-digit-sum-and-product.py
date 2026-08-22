class Solution:
    def checkDivisibility(self, n: int) -> bool:
        nums = str(n)
        sums = 0
        product = int(nums[0])

        for s in nums:
            sums += int(s)
        for i in range(1, len(nums)):
            product *= int(nums[i])

        target = sums + product

        if n % target == 0:
            return True
            
        return False 



            
            



        