# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Runtime: 36 ms, faster than 69.03% of Python3 online submissions for Reverse Linked List.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Reverse Linked List.
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        while current:
            following = current.next
            current.next = prev
            prev = current
            current = following
        return prev
