class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for string in strs:
            freq = [0] * 26
            for ch in string:
                idx = ord(ch) - ord('a')
                freq[idx] += 1
            tupfreq = tuple(freq)
            if tupfreq in dic:
                dic[tupfreq].append(string)
            else:
                dic[tupfreq] = [string]
        
        ans = []
        for key in dic:
            ans.append(dic[key])
        return ans
