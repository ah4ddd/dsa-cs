from math import gcd

class Solution:
    def findKthSmallest(self, coins, k):

        def count(x):
            total = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        lcm = lcm * coins[i] // gcd(lcm, coins[i])
                        bits += 1

                        if lcm > x:
                            break

                if lcm <= x:
                    if bits % 2:
                        total += x // lcm
                    else:
                        total -= x // lcm

            return total

        left, right = 1, min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left