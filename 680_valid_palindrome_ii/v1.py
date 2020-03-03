'''
Runtime: 100 ms, faster than 83.53% of Python3 online submissions for Valid Palindrome II.
Memory Usage: 13.2 MB, less than 62.50% of Python3 online submissions for Valid Palindrome II.
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s)-1
        
        while lo < hi:
            if s[lo] != s[hi]:
                # remove s[lo]
                can1 = s[:lo] + s[lo+1:]
                # remove s[hi]
                can2 = s[:hi] + s[hi+1:]
                return can1 == can1[::-1] or can2 == can2[::-1]
            else:
                lo += 1
                hi -= 1
                
        return True
