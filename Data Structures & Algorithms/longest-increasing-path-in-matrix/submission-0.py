class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]

        def dfs(r, c):
            if dp[r][c] != -1:
                return dp[r][c]

            maxlen = 1
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = dr + r, dc + c

                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[r][c] < matrix[nr][nc]:
                    maxlen = max(maxlen, dfs(nr, nc) + 1)
                
            dp[r][c] = maxlen
            return maxlen
        
        ans = 1  
        for r in range(len(dp)):
            for c in range(len(dp[0])):
                ans = max(ans, dfs(r, c))
        return ans