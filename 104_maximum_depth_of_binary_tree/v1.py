# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Runtime: 36 ms, faster than 88.03% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Maximum Depth of Binary Tree.
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
