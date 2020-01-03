'''
Runtime: 36 ms, faster than 97.98% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays.
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
