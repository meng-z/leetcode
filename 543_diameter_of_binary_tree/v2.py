# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Runtime: 44 ms, faster than 67.77% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Diameter of Binary Tree.
'''
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.ans = 0
        def depth(root):
            if root is None:
                return 0
            
            left = depth(root.left)
            right = depth(root.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1
        
        depth(root)
        return self.ans
