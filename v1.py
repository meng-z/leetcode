from collections import defaultdict
import re

'''
Runtime: 32 ms, faster than 69.73% of Python3 online submissions for Most Common Word.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Most Common Word.
'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # lower paragraph
        paragraph = paragraph.lower()
        words = re.split('[!?\',;.\s]', paragraph)
        
        word_occur = defaultdict(int)
        for word in words:
            if len(word) == 0:
                continue
            if word not in banned:
                word_occur[word] += 1
     
        most_occur_word = ''
        max_occur = 0
        for word, occur in word_occur.items():
            if occur > max_occur:
                max_occur = occur
                most_occur_word = word
                
        return most_occur_word
