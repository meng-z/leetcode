'''
Runtime: 48 ms, faster than 61.05% of Python3 online submissions for Valid Palindrome.
Memory Usage: 13.1 MB, less than 96.43% of Python3 online submissions for Valid Palindrome.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        no_punc = ''
        for char in s:
            # can use isalnum() instead
            if char.isalpha() or char.isdigit():
                no_punc += char.lower()
      
        return True if no_punc == no_punc[::-1] else False
