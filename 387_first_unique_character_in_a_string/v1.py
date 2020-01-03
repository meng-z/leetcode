'''
Runtime: 184 ms, faster than 13.74% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for First Unique Character in a String.
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, e in enumerate(s):
            if e in d:
                d[e] = (d[e][0]+1, d[e][1])
            else:
                d[e] = (1, i)

        res = {e:v[1] for e, v in d.items() if v[0] == 1}
        if len(res) == 0:
            return -1
        else:
            return sorted(res.items(), key=lambda x:x[1])[0][1]
