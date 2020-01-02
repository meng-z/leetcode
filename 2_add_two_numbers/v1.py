# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Runtime: 72 ms, faster than 61.65% of Python3 online submissions for Add Two Numbers.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # use another linked list to store the result
        dummy = ListNode(0)
        
        prev = dummy
        prev_upgrade = 0
        while True:
            upgrade = 0
            if l1 and l2:
                upgrade = (prev_upgrade + l1.val + l2.val) // 10
                value = (prev_upgrade + l1.val + l2.val) % 10
                prev_upgrade = upgrade
                l1 = l1.next
                l2 = l2.next
                
            elif l1 and not l2:
                upgrade = (prev_upgrade + l1.val) // 10
                value = (prev_upgrade + l1.val) % 10
                prev_upgrade = upgrade
                l1 = l1.next
                
            elif not l1 and l2:
                upgrade = (prev_upgrade + l2.val) // 10
                value = (prev_upgrade + l2.val) % 10
                prev_upgrade = upgrade
                l2 = l2.next
                
            else:
                break
              
            current = ListNode(value)
            prev.next = current
            prev = current
         
        if prev_upgrade != 0:
            current = ListNode(prev_upgrade)
            prev.next = current
            
        return dummy.next
