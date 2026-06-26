class Solution:
    def partition(self, s: str) -> List[List[str]]:
        combos = []

        def ispalindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - i - 1]:
                    return False
            return True
        
        def backtrack(start, pallist):
            if start == len(s):
                combos.append(pallist)
                return
            
            for i in range(start + 1, len(s) + 1):
                if ispalindrome(s[start:i]):
                    backtrack(i, pallist + [s[start:i]])
        backtrack(0, [])
        return combos