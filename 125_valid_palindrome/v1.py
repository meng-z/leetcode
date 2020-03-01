'''
Runtime: 52 ms, faster than 44.72% of Python3 online submissions for Valid Palindrome.
Memory Usage: 13.1 MB, less than 97.62% of Python3 online submissions for Valid Palindrome.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        lo, hi = 0, len(s)-1
        flag = 0
        while lo < hi:
            lo_char = s[lo].lower()
            hi_char = s[hi].lower()

            # if char is not alphanumeric, modify lo/hi
            if not lo_char.isalpha() and not lo_char.isdigit():
                lo += 1
                flag = 1
            if not hi_char.isalpha() and not hi_char.isdigit():
                hi -= 1
                flag = 1
              
            if not flag:
                if lo_char == hi_char:
                    lo += 1
                    hi -= 1
                    flag = 0
                else:
                    return False
            flag = 0

        return True
