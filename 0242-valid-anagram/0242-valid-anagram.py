class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c1 = {}
        c2 = {}

        for w in s:
            if w in c1:
                c1[w] += 1
            else:
                c1[w] = 1

        for x in t:
            if x in c2:
                c2[x] += 1
            else:
                c2[x] = 1

        return c1 == c2