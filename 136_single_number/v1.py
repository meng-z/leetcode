'''
Runtime: 72 ms, faster than 63.46% of Python online submissions for Single Number.
Memory Usage: 14.7 MB, less than 5.40% of Python online submissions for Single Number.
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
            
        return nums[0]
