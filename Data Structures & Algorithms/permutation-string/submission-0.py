class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = [0] * 26
        for i in s1:
            freq[ord(i) - 97] += 1

        freq2 = [0] * 26
        for i in range(len(s1)):
            freq2[ord(s2[i]) - 97] += 1
        if freq == freq2:
            return True
        
        for i in range(len(s1), len(s2)):
            freq2[ord(s2[i]) - 97] += 1
            freq2[ord(s2[i-len(s1)]) - 97] -= 1

            if freq2 == freq:
                return True
        
        return False