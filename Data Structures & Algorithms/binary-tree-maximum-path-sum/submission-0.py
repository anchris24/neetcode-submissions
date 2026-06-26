# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = [root.val]

        def sumsub(node):
            if not node:
                return 0
            
            leftsum = max(0, sumsub(node.left))
            rightsum = max(0, sumsub(node.right))

            maxsum[0] = max(maxsum[0], node.val + leftsum + rightsum)

            return node.val + max(leftsum, rightsum)
        
        sumsub(root)
        return maxsum[0]
