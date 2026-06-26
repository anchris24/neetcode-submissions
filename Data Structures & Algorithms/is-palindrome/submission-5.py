class Solution:
    def isPalindrome(self, s: str) -> bool:
        validchars = "qwertyuiopasdfghjklzxcvbnm1234567890"
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            while l < len(s) and s[l] not in validchars:
                l += 1
            while r >= 0 and s[r] not in validchars:
                r -= 1

            if not (l < len(s) and r >= 0):
                return True

            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True
