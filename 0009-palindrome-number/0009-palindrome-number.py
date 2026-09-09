class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)

        for i in range(len(num)//2):
            if num[i] != num[len(num) - 1 - i]:
                return False

        return True