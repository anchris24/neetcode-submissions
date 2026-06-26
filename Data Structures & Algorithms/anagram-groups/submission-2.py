class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getFreq(s):
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1
            return tuple(freq)
        
        freqmap = {}
        for word in strs:
            freq = getFreq(word)
            if freq in freqmap:
                freqmap[freq].append(word)
            else:
                freqmap[freq] = [word]
        
        return [freqmap[freq] for freq in freqmap]