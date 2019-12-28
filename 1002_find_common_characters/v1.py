from collections import defaultdict

'''
Runtime: 32 ms, faster than 91.58% of Python online submissions for Find Common Characters.
Memory Usage: 12.4 MB, less than 5.88% of Python online submissions for Find Common Characters.
'''
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        char_list = list()
        for term in A:
            char_num_in_term = defaultdict(int)
            for char in term:
                char_num_in_term[char] += 1
                
            char_list.append(char_num_in_term)
            
        char_list_keys = [set(cl.keys()) for cl in char_list]
        common_chars = set.intersection(*char_list_keys)
        final_common_chars = {common_char: char_list[0][common_char] for common_char in common_chars}
        for common_char in common_chars:
            for cl in char_list:
                if cl[common_char] < final_common_chars[common_char]:
                    final_common_chars[common_char] = cl[common_char]
                    
        final_result = list()
        for k, v in final_common_chars.items():
            final_result += k*v
            
        return final_result
