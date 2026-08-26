class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magz = {}

        for m in magazine:
            if m in magz:
                magz[m] += 1
            else:
                magz[m] = 1

        for r in ransomNote:
            if r in magz and magz[r] > 0:
                magz[r] -= 1
            else:
                return False
                
        return True





        
        