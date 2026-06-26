# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ids = {}
        for i in range(len(inorder)):
            ids[inorder[i]] = i

        preid = [0]
        def dfs(left, right):
            if left > right:
                return None
            
            root = TreeNode(preorder[preid[0]])
            splitid = ids[preorder[preid[0]]]

            preid[0] += 1
            root.left = dfs(left, splitid - 1)
            root.right = dfs(splitid + 1, right)
           
            return root
        return dfs(0, len(preorder) - 1)