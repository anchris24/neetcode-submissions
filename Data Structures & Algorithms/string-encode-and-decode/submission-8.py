class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string
        return s

    def decode(self, s: str) -> List[str]:
        ans = []
        idx = 0
        print(s)
        
        while idx < len(s):

            j = idx
            while s[j] != "#":
                j += 1
            
            length = int(s[idx:j])
            ans.append(s[j+1: j + length + 1])

            idx = j + length + 1

        return ans

        