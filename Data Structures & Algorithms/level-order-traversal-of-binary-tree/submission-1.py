# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        traversal = []

        queue = deque([root])
        while queue:
            size = len(queue)
            level = []

            for i in range(size):
                curr = queue.popleft()
                if not curr:
                    continue
                level.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            
            if level:
                traversal.append(level)
            else:
                return traversal
