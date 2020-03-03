'''
Runtime: 40 ms, faster than 22.30% of Python3 online submissions for Verifying an Alien Dictionary.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Verifying an Alien Dictionary.
'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # also tried string.ascii_lowercase, but seems string cannot be imported
        original = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        
        # a map from alien to original order
        alien2original = {k:v for k, v in zip(order, original)}
        # i is the position in given words
        words_extended = [(i, word, ''.join([alien2original[char] for char in word])) for i, word in enumerate(words)]
        
        sorted_words_extended = sorted(words_extended, key=lambda x:x[2])
        
        for i, swe in enumerate(sorted_words_extended):
            if i != swe[0]:
                return False
            
        return True
