# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def backtrack(node, minm, maxm):
            if not node:
                return True
            
            if minm < node.val < maxm:
                return backtrack(node.left, minm, node.val) and backtrack(node.right, node.val, maxm)
            return False

        return backtrack(root, -1000, 1000)