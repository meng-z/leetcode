'''
Runtime: 40 ms, faster than 61.17% of Python3 online submissions for Bulls and Cows.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Bulls and Cows.
'''
from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        res_secret, res_guess = '', ''
        counter = Counter(secret)
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
                counter[s] -= 1
            else:
                res_secret += s
                res_guess += g

        for g in res_guess:
            if g in res_secret and counter[g] > 0:
                cows += 1
                counter[g] -= 1
                    
        return '{}A{}B'.format(bulls, cows)
