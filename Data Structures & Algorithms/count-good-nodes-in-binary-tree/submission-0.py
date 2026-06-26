# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]

        def backtrack(node, maxm):
            if not node:
                return

            if node.val >= maxm:
                count[0] += 1
            
            backtrack(node.left, max(maxm, node.val))
            backtrack(node.right, max(maxm, node.val))

        backtrack(root, root.val)
        return count[0]
