'''
Runtime: 24 ms, faster than 95.27% of Python3 online submissions for Add Binary.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Add Binary.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        
        carry, ans = 0, []
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            
            if b[i] == '1':
                carry += 1
                
            if carry % 2 == 1:
                ans.append('1')
            else:
                ans.append('0')
                
            carry = carry // 2
          
        if carry == 1:
            ans.append('1')

        return ''.join(ans[::-1])
