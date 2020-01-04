'''
Runtime: 28 ms, faster than 65.26% of Python3 online submissions for Pow(x, n).
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Pow(x, n).
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        half = self.myPow(x, int(n / 2)) # note that -1//2 results in -1
        if n % 2 == 0:
            return half * half
        else:
            if n > 0:
                return half * half * x
            else:
                return (half * half) / x
