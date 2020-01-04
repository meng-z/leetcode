'''
Runtime: 40 ms, faster than 57.81% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i + 1 > len(nums) - 1:
                return nums[0]
            
            # the first place that num does not increase
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
