class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1
            
            freqtuple = tuple(freq)
            if freqtuple in dic:
                dic[freqtuple].append(s)
            else:
                dic[freqtuple] = [s]
        
        ans = []
        for key in dic:
            ans.append(dic[key])
        return ans