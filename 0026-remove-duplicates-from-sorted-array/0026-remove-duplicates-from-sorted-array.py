class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Points to the next position where a unique number should be written.
        unique_pos = 1
        
        for cur in range(1, len(nums)):
            if nums[cur] != nums[cur - 1]:
                nums[unique_pos] = nums[cur]
                unique_pos += 1
                
        return unique_pos
