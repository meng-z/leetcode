from heapq import *

'''
Runtime: 224 ms, faster than 31.92% of Python3 online submissions for Find K Pairs with Smallest Sums.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Find K Pairs with Smallest Sums.
'''
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        for n1 in nums1:
            for n2 in nums2:
                if len(h) >= k:
                    heappushpop(h, (-(n1 + n2), [n1, n2]))
                else:
                    heappush(h, (-(n1 + n2), [n1, n2]))
                    
        return [heappop(h)[1] for i in range(len(h))]
