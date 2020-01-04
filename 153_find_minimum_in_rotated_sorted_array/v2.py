'''
Runtime: 36 ms, faster than 83.22% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        
        return nums[hi] # the same as return nums[lo]
