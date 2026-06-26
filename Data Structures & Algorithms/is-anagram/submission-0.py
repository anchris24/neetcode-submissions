class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for ch in s:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1
        
        for ch2 in t:
            if not ch2 in dic:
                return False
            
            if dic[ch2] == 1:
                dic.pop(ch2)
            else:
                dic[ch2] -= 1
        
        if dic:
            return False
        return True