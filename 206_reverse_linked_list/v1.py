# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Runtime: 36 ms, faster than 69.03% of Python3 online submissions for Reverse Linked List.
Memory Usage: 14.9 MB, less than 31.82% of Python3 online submissions for Reverse Linked List.
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        after = ListNode(head.val)
        while head.next:
            current = ListNode(head.next.val)
            current.next = after
            after = current
            head = head.next
            
        return current
