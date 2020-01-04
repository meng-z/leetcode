'''
Runtime: 44 ms, faster than 25.30% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 13.1 MB, less than 94.41% of Python3 online submissions for Search in Rotated Sorted Array.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        def binary_search(nums, target, lo, hi):
            mid = (lo + hi) // 2
            
            if nums[mid] == target:
                return mid
            
            if lo > hi:
                return -1
            
            # left part is sorted
            if nums[mid] > nums[hi]:
                # target beyond the range of left part
                if target < nums[lo] or target > nums[mid]:
                    mid = binary_search(nums, target, mid + 1, hi)
                else:
                    mid = binary_search(nums, target, lo, mid - 1)
            else:
                if target < nums[mid] or target > nums[hi]:
                    mid = binary_search(nums, target, lo, mid - 1)
                else:
                    mid = binary_search(nums, target, mid + 1, hi)
            return mid
        
        return binary_search(nums, target, 0, len(nums) - 1)
