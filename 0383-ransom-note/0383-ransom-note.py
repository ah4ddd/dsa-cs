#  pass it a string, it automatically counts the frequency of every single character
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magz = Counter(magazine)

        for r in ransomNote:
            if r in magz and magz[r] > 0:
                magz[r] -= 1
            else:
                return False
                
        return True





        
        