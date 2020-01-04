# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Runtime: 76 ms, faster than 11.79% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.2 MB, less than 100.00% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def generateBST(root, lo, hi):
            if lo > hi:
                return
            
            mid = (lo + hi) // 2
            root = TreeNode(nums[mid])
            root.left = generateBST(root.left, lo, mid - 1)
            root.right = generateBST(root.right, mid + 1, hi)
            
            return root
        
        res = generateBST(None, 0, len(nums) - 1)
        return res
