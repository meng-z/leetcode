# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Runtime: 52 ms, faster than 57.05% of Python3 online submissions for Linked List Cycle.
Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
Solve it using O(1) memory.
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        
        fast = head
        slow = head
        
        while slow is not None:
            if fast.next is None or fast.next.next is None:
                return False
            
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
            
        return False
