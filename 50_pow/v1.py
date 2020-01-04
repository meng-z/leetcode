'''
Runtime Error
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n > 0:
            res = self.myPow(x, n - 1) * x
        else:
            res = self.myPow(x, n + 1) * (1 / x)
            
        return res
