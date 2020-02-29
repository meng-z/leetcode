'''
Runtime: 40 ms, faster than 77.21% of Python3 online submissions for Two Sum Less Than K.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Two Sum Less Than K.
'''
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        n = len(A)
        if n < 2:
            return -1
        
        # sort array A
        sorted_A = sorted(A)
        
        ans, best = -1, float('inf')
        lo, hi = 0, n - 1
        while lo < hi:
            val = sorted_A[lo] + sorted_A[hi]
            if val >= K:
                hi = hi - 1
            else:
                lo = lo + 1
                
            diff = K - val
            if diff > 0 and diff < best:
                ans, best = val, diff
                
        return ans
