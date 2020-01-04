# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Runtime: 48 ms, faster than 24.22% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 15.1 MB, less than 62.16% of Python3 online submissions for Minimum Depth of Binary Tree.
'''
class Solution:        
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.depth = float('inf')
        
        def dfs(node, d):
            if not node:
                return
            if not node.left and not node.right:
                self.depth = min(self.depth, d)
            if node.left:
                dfs(node.left, d + 1)
            if node.right:
                dfs(node.right, d + 1)
                
        dfs(root, 1)
        return self.depth
