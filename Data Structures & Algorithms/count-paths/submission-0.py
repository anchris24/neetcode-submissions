class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = 1
        for i in range(1, n):
            ans *= (m+n-1-i)
            ans //= i
        return int(ans)