'''
Runtime: 40 ms, faster than 73.28% of Python3 online submissions for Add Strings.
Memory Usage: 13 MB, less than 94.44% of Python3 online submissions for Add Strings.
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # a map from char to digit
        char2digit = {str(i):i for i in range(10)}
        n = max(len(num1), len(num2))
        num1 = num1.zfill(n)
        num2 = num2.zfill(n)
        
        carry = 0
        ans = []
        for i in range(n-1, -1, -1):
            carry += char2digit[num1[i]] + char2digit[num2[i]]
            ans.append(str(carry % 10))
            carry = carry // 10
            
        if carry == 1:
            ans.append('1')
            
        return ''.join(ans[::-1])
