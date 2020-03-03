'''
Runtime: 656 ms, faster than 7.74% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Diameter of Binary Tree.
'''
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        def depth(root):
            if root is None:
                return 0
            
            return max(depth(root.left), depth(root.right)) + 1
        
        longest = 0
        queue = deque([root])
        while queue:
            current = queue.popleft()
            candidate_path = depth(current.left) + depth(current.right)
            if candidate_path > longest:
                longest = candidate_path
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
                
        return longest
