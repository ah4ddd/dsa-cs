class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        
        for a in arr:
            if a * 2 in seen:
                return True
            elif a % 2 == 0 and a // 2 in seen:
                return True
            else:
                seen.add(a)
                
        return False