# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        layer = [root]
        right = []

        while layer:
            # rightfound = False
            # r = None

            l = len(layer)
            for i in range(l):
                curr = layer.pop(0)
                if i == l-1:
                    right.append(curr.val)
                if curr.left:
                    layer.append(curr.left)
                if curr.right:
                    layer.append(curr.right)
            
            # if rightfound:
            #     right.append(r)
        
        return right