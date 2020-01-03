from collections import defaultdict

'''
Runtime: 112 ms, faster than 37.33% of Python3 online submissions for Group Anagrams.
Memory Usage: 16 MB, less than 60.38% of Python3 online submissions for Group Anagrams.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for s in strs:
            key = str(sorted([char for char in s]))
            dd[key].append(s)
            
        return list(dd.values())
