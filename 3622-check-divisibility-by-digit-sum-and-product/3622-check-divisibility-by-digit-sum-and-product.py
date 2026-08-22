class Solution:
    def checkDivisibility(self, n: int) -> bool:
        nums = str(n)
        sums = 0
        product = 1

        for s in nums:
            digit = int(s)
            sums += digit
            product *= digit

        target = sums + product
        return n % target == 0