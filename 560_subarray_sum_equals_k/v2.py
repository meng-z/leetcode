from collections import defaultdict

'''
Runtime: 108 ms, faster than 92.52% of Python3 online submissions for Subarray Sum Equals K.
Memory Usage: 16.8 MB, less than 20.00% of Python3 online submissions for Subarray Sum Equals K.
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            target = prefix_sum - k
            count += d[target]
            d[prefix_sum] += 1
                    
        return count
