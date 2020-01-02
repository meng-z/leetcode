'''
Runtime: 24 ms, faster than 94.35% of Python3 online submissions for Valid Parentheses.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        if len(s) % 2 != 0:
            return False
        
        stack = list()
        parentheses = {'(': ')', '[':']', '{': '}'}
        for e in s:
            if e in parentheses.keys():
                stack.append(e)
            elif stack and e in parentheses.values():
                current = stack.pop()
                if e != parentheses[current]:
                    return False
            else:
                return False
                
        return stack == []
