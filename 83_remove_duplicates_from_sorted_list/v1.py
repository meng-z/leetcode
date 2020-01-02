# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Runtime: 36 ms, faster than 91.92% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List.
'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        tmp = head
        while tmp.next is not None:
            next_node = tmp.next
            if tmp.val == next_node.val:
                skipped_des = next_node.next
                next_node.next = None
                tmp.next = skipped_des
                del next_node
            else:
                tmp = next_node
            
        return head
