from collections import defaultdict

'''
Runtime: 116 ms, faster than 56.89% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for First Unique Character in a String.
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(int)
        for e in s:
            d[e] += 1

        for i, e in enumerate(s):
            if d[e] == 1:
                return i
            
        return -1
