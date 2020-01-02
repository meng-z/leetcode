# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Time Limit Exceeded.
'''
class Solution:
    def index(self, scanned: ListNode, a: ListNode) -> ListNode:
        for i, node in enumerate(scanned):
            if node == a:
                return node
        return None
        
        
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        scanned = []
        while head.next is not None:
            tmp = self.index(scanned, head)
            if tmp is not None:
                return tmp
            
            scanned.append(head)
            head = head.next
            
        return None
