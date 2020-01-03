from collections import defaultdict

'''
Runtime: 92 ms, faster than 95.40% of Python3 online submissions for Group Anagrams.
Memory Usage: 15.7 MB, less than 92.45% of Python3 online submissions for Group Anagrams.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for s in strs:
            dd[''.join(sorted(s))].append(s)
            
        return list(dd.values())
