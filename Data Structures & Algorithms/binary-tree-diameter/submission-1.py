# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiam = [0]

        def depth(start):
            if not start:
                return 0
            else:
                left = depth(start.left)
                right = depth(start.right)
                maxdiam[0] = max(left + right, maxdiam[0])
                return max(left, right) + 1
        depth(root)
        return maxdiam[0] 