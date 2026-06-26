class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        prev, curr = [0] * (len(t) + 1), [0] * (len(t) + 1)
        prev[0] = 1

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i-1] == t[j-1]:
                    curr[j] = prev[j] + prev[j-1]
                else:
                    curr[j] = prev[j]
            
            prev, curr = curr, prev
            prev[0] = 1
        
        return prev[-1]