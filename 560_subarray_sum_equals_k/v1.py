'''
Time Limit Exceeded
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:        
        count = 0

        for i in range(len(nums)):
            # j is the window size
            for j in range(1, len(nums) - i + 1):
                tmp = sum(nums[i:i+j])
                #print(i, j, tmp, nums[i:i+j])
                if tmp == k:
                    count += 1
                    
        return count
