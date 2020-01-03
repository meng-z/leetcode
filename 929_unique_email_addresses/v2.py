'''
Runtime: 44 ms, faster than 92.15% of Python3 online submissions for Unique Email Addresses.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Unique Email Addresses.
'''
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:    
        distinct = set()
        for email in emails:
            local, domain = email.split('@')
            plus = local.split('+')
            distinct.add(plus[0].replace('.', '')+'@'+domain)
            
        return len(distinct)
