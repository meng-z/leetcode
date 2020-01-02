# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
2(x + y) = x + y + z + y => x = z
x: distance between head node and cycle begin node
y: distance from cycle begin node to crossed node
z: distance from crossed node to cycle begin node

Runtime: 40 ms, faster than 99.03% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.
'''
class Solution:        
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        fast = head
        slow = head
        
        while True:
            if fast.next is None or fast.next.next is None:
                return None
            
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
                
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow
