class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_pos = 1
        
        for c in range(1, len(nums)):
            if nums[c] != nums[c-1]:
                nums[unique_pos] = nums[c]
                unique_pos += 1

        return unique_pos


