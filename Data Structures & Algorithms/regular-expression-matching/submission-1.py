class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        idx = 1
        while idx < len(p):
            if p[idx] == '*':
                dp[0][idx+1] = True
            else:
                break
            idx += 2


        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]

                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] |= dp[i-1][j]
        
        return dp[-1][-1]
