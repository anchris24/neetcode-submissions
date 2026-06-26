class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        substr = set()

        i, j = 0, 0
        while i < len(s) and j < len(s):
            if s[j] in substr:
                while s[i] != s[j]:
                    substr.remove(s[i])
                    i+=1
                substr.remove(s[i])
                i+=1
  
            substr.add(s[j])
            j += 1
            
            maxlen = max(maxlen, len(substr))
        return maxlen