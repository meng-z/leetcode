'''
Runtime: 48 ms, faster than 78.67% of Python3 online submissions for Two Sum.
Memory Usage: 14.2 MB, less than 54.18% of Python3 online submissions for Two Sum.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # in the format complement:index of original num
        complement = {}
        
        for i, num in enumerate(nums):
            a = target - num

            if num in complement:
                return [complement[num], i]
            else:
                complement[a] = i
