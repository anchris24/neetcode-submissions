# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 'null'
        
        ans = []
        queue = deque()
        queue.append(root)

        while queue:
            curr = queue.popleft()
            if not curr:
                ans.append('null')
                continue

            ans.append(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)
        
        return ",".join(map(str, ans))
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == 'null':
            return None

        tree = data.split(",")
        queue = deque()
        root = TreeNode(int(tree[0]))
        queue.append( root )
        idx = 1
        while queue:
            curr = queue.popleft()

            if tree[idx] != 'null':
                curr.left = TreeNode(int(tree[idx]))
                queue.append(curr.left)
            idx += 1

            if tree[idx] != 'null':
                curr.right = TreeNode(int(tree[idx]))
                queue.append(curr.right)
            idx += 1

        return root

