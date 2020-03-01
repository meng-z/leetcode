'''
Runtime: 28 ms, faster than 84.26% of Python3 online submissions for Add Binary.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Add Binary.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na = int(a, 2)
        nb = int(b, 2)
        # note that the parameter you pass to the .format must be of type int
        return str(format(na + nb, 'b'))
