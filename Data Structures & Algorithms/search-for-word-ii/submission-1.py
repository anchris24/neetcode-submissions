class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        root = Node()

        i = 0
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = Node()
                curr = curr.children[ch]
            curr.end = True
            curr.idx = i
            i += 1

        visited = set()
        ans = []
        def dfs(r, c, node):
            if not (0 <= r < len(board) and 0 <= c < len(board[0])) or board[r][c] not in node.children or (r, c) in visited:
                
                return 
            
            node = node.children[board[r][c]]
            if not node.haswords:
                return 
                
            visited.add( (r, c) )
            if node.end:
                node.end = False
                ans.append(words[node.idx])
                if not any(child.haswords for child in node.children.values()):
                    node.haswords = False

            for dr, dc in directions:
                dfs(dr + r, dc + c, node)

            visited.remove( (r, c) )
        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root)

        return ans



class Node:

    def __init__(self):
        self.children = {}
        self.end = False
        self.idx = -1
        self.haswords = True