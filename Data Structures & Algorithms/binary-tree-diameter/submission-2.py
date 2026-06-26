# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxdiameter = [0]
        
        def finddepth(node):
            if not node:
                return 0

            left = finddepth(node.left)
            right = finddepth(node.right)

            maxdiameter[0] = max(maxdiameter[0], left + right)
            return max(left, right) + 1
        
        finddepth(root)
        return maxdiameter[0]