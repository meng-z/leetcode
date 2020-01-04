'''
Runtime: 48 ms, faster than 73.77% of Python3 online submissions for Search Insert Position.
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Search Insert Position.
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # adding if condition to solve corner case improved runtime
        if not nums or target <= nums[0]:
            return 0

        if target > nums[len(nums) - 1]:
            return len(nums)

        def binarySearch(l, val, lo, hi):
            # when lo becomes larger than hi, it is the right pos to insert
            if lo > hi:
                return lo

            mid = (lo + hi) // 2

            if l[mid] > val:
                return binarySearch(l, val, lo, mid - 1)
            elif l[mid] < val:
                return binarySearch(l, val, mid + 1, hi)
            else:
                return mid

        return binarySearch(nums, target, 0, len(nums) - 1)
