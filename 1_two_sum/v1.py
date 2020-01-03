'''
Runtime: 6020 ms, faster than 10.78% of Python3 online submissions for Two Sum.
Memory Usage: 13.6 MB, less than 91.63% of Python3 online submissions for Two Sum.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        return []
