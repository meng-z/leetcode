'''
Runtime: 64 ms, faster than 96.93% of Python3 online submissions for Subtree of Another Tree.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Subtree of Another Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        # do DFS in pre-order traversal
        def preorder(root):
            return '#{} {} {}'.format(root.val, preorder(root.left), preorder(root.right)) if root else 'null'
        
        s_traversal = preorder(s)
        t_traversal = preorder(t)

        if t_traversal in s_traversal:
            return True
        else:
            return False
