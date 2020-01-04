'''
Time Limit Exceeded
'''
class Solution:
    def _rowN(self, N: int) -> str:
        # generate the row N
        if N == 1:
            return '0'
        
        return self._transform(self._rowN(N - 1))
        
    def _transform(self, s: str) -> str:
        res = ''
        for char in s:
            res += self.grammar[char]
        return res
        
    def kthGrammar(self, N: int, K: int) -> int:
        self.grammar = {'0': '01', '1': '10'}
        row_n = self._rowN(N)
        return int(row_n[K - 1])
