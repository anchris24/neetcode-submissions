class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []

        def backtrack(s, opencnt, closecnt):
            if opencnt == n and closecnt == n:
                ans.append(s)
                return 
            
            if opencnt < n:
                backtrack(s + '(', opencnt + 1, closecnt)
            if opencnt > closecnt:
                backtrack(s + ')', opencnt, closecnt + 1)

        backtrack("", 0, 0)
        return ans