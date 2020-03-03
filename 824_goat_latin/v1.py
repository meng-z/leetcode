'''
Runtime: 20 ms, faster than 96.15% of Python3 online submissions for Goat Latin.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Goat Latin.
'''
class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = set('aeiou')
        suffix = 'ma'
        words = S.split()
        ans = []
        for i, word in enumerate(words):
            if word[0].lower() in vowels:
                word = word + suffix
            else:
                word = word[1:] + word[0] + suffix
                
            word += 'a'*(i+1)
            ans.append(word)
            
        return ' '.join(ans)
