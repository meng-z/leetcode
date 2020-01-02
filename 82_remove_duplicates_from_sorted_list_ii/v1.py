# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Runtime: 36 ms, faster than 90.74% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List II.
'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        # add a tmp node pointed to the head node
        first = ListNode(head.val - 1)
        first.next = head
        prev = first
        current = head
        
        # count for duplicates
        duplicate = 1
        while current.next:
            if current.val == current.next.val:
                current = current.next
                duplicate += 1
            else:
                if duplicate > 1:
                    prev.next = current.next
                    current = current.next
                    duplicate = 1
                else:
                    prev = current
                    current = current.next
                    duplicate = 1
           
        # special case like [1,2,2]
        if duplicate > 1:
            prev.next = current.next
        
        return first.next
