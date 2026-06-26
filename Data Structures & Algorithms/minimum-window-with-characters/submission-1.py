class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""

        freqt = {}
        for ch in t:
            freqt[ch] = freqt.get(ch, 0) + 1
        
        subfreq = {}
        left = 0
        req, formed = len(freqt), 0
        ans, length  = "", float("inf")

        for right in range(len(s)):
            subfreq[s[right]] = subfreq.get(s[right], 0) + 1
            if s[right] in freqt and subfreq[s[right]] == freqt[s[right]]:
                formed += 1
            
            while formed == req:
                if s[left] in freqt and subfreq[s[left]] == freqt[s[left]]:
                    formed -= 1
                subfreq[s[left]] -= 1
                
                if right - left < length:
                    length = right - left
                    ans = s[left:right+1]

                left += 1

        return ans
