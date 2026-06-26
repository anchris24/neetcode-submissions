class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ans = ""
        id1, id2 = 0, 0
        while id1 < len(word1) and id2 < len(word2):
            ans += word1[id1]
            ans += word2[id2]

            id1 += 1
            id2 += 1
        
        ans += word1[id1:]
        ans += word2[id2:]
    
        return ans
