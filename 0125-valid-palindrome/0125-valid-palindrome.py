class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for c in s:
            if c.isalnum():
                chars.append(c.lower())

        clean = ''.join(chars)

        for i in range(len(clean)//2):
            if clean[i] != clean[-(i+1)]:
                return False

        return True