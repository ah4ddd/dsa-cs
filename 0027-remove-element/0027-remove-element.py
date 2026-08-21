class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new = []
        
        for n in nums:
            if n == val:
                continue
            else:
                new.append(n)
        nums[:] = new

        return len(nums)