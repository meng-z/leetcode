# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Runtime: 1212 ms, faster than 5.03% of Python3 online submissions for Linked List Cycle.
Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
Failed to solve it using O(1) (i.e. constant) memory.
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        
        scanned = []
        while head.next is not None:
            if head in scanned:
                return True
            
            scanned.append(head)
            head = head.next
        
        return False
