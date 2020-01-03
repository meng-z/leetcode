from collections import defaultdict

'''
Runtime: 52 ms, faster than 55.75% of Python3 online submissions for Two Sum.
Memory Usage: 15.5 MB, less than 5.11% of Python3 online submissions for Two Sum.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # duplicates may exist
        item2idx = defaultdict(list)
        for i,num in enumerate(nums):
            item2idx[num].append(i)

        sorted_nums = sorted(nums)
        for i, num in enumerate(sorted_nums):
            partner = target - num
            if partner in sorted_nums:
                idx = sorted_nums.index(partner)
                break
         
        if i == idx:
            return item2idx[sorted_nums[i]]
        else:
            return [item2idx[sorted_nums[i]][0], item2idx[sorted_nums[idx]][0]]
