class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combos = []
        
        def backtrack(opens, closed, path):
            if opens + closed == 2*n:
                combos.append(path)
                return
            
            if opens > closed:
                backtrack(opens, closed + 1, path + ")")
            if opens < n:
                backtrack(opens + 1, closed, path + "(")
        
        backtrack(0, 0, "")
        return combos

