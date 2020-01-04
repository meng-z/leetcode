'''
Runtime: 24 ms, faster than 87.19% of Python3 online submissions for K-th Symbol in Grammar.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for K-th Symbol in Grammar.
'''
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1 or K == 1:
            return 0
        
        # depend on K//2 in row N-1
        if K % 2 == 1:
            return self.kthGrammar(N - 1, K//2 + 1)
        else:
            if self.kthGrammar(N - 1, K//2) == 1:
                return 0
            else:
                return 1
