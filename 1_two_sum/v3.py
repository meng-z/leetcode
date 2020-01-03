'''
Runtime: 48 ms, faster than 78.88% of Python3 online submissions for Two Sum.
Memory Usage: 14.4 MB, less than 34.65% of Python3 online submissions for Two Sum.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        item2idx = {num:i for i, num in enumerate(nums)}
        
        for i, num in enumerate(nums):
            partner = target - num
            if partner in item2idx.keys() and item2idx[partner] != i:
                return [i, item2idx[partner]]
            
        return []
