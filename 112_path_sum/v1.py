# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Runtime: 40 ms, faster than 77.68% of Python3 online submissions for Path Sum.
Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Path Sum.
'''
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        def check(root, target_sum, current_sum):
            if not root:
                return False
            
            # reach the leaf
            if root.left is None and root.right is None and current_sum + root.val == target_sum:
                return True
            
            return check(root.left, target_sum, current_sum + root.val) or check(root.right, target_sum, current_sum + root.val)
        
        return check(root, sum, 0)
