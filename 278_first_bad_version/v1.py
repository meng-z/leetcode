# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

'''
Runtime: 24 ms, faster than 84.54% of Python3 online submissions for First Bad Version.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for First Bad Version.
'''
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # binary search for first bad version
        lo, hi = 1, n
        while lo < hi:
            middle = (lo + hi) // 2
            if isBadVersion(middle):
                hi = middle
            else:
                lo = middle + 1
                
        return lo
