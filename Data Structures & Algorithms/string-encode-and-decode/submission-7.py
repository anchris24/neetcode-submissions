from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Find the position of the next #
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            j += 1  # Move past '#'
            word = s[j:j + length]
            res.append(word)
            i = j + length
        return res
