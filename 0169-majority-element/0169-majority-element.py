class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        return max(count, key=count.get)

        """ # dropped but works
        major_freq = float("-inf")
        major_elm = None


        for k, v in count.items():
            if v > major_freq:    
                major_freq = v
                major_elm = k

        return major_elm
        """
