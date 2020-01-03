from collections import defaultdict

'''
Runtime: 48 ms, faster than 77.79% of Python3 online submissions for Unique Email Addresses.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Unique Email Addresses.
'''
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dd = defaultdict(int)
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')].replace('.', '')
            else:
                local = local.replace('.', '')
                
            dd[local+'@'+domain] += 1
            
        return len(dd.keys())
