class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringset = set()
        i, j = 0, 0
        maxlen = 0
        while i < len(s) and j < len(s):
            while s[j] in stringset:
                stringset.remove(s[i])
                i += 1
            stringset.add(s[j])
            j += 1
            maxlen = max(maxlen, j-i)
        
        return maxlen
                