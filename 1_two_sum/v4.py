'''
Runtime: 48 ms, faster than 78.88% of Python3 online submissions for Two Sum.
Memory Usage: 14 MB, less than 65.81% of Python3 online submissions for Two Sum.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        item2idx = {}
        
        for i, num in enumerate(nums):
            if (target - num) in item2idx:
                return [i, item2idx[target - num]]
            item2idx[num] = i
            
        return []
