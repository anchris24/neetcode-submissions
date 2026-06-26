# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        maxm = [0]

        if root is None:
            return 0
        
        def depth(node, curr):
            if node is None:
                maxm[0] = max(maxm[0], curr)
                return 
            
            depth(node.left, curr + 1)
            depth(node.right, curr + 1)
        
        depth(root, 0)
        return maxm[0]
            
