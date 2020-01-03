from collections import Counter

'''
Runtime: 100 ms, faster than 92.52% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 17.2 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre_counter = Counter(nums)
        most_fre = []
        for e in fre_counter.most_common(k):
            most_fre.append(e[0])
            
        return most_fre
