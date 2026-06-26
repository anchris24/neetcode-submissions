class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        length = len(s1)
        freq1 = [0] * 26
        for c in s1:
            freq1[ord(c) - ord('a')] += 1

        freq2 = [0] * 26
        for c in s2[:length]:
            freq2[ord(c) - ord('a')] += 1

        if freq1 == freq2:
            return True

        for idx in range(length, len(s2)):
            freq2[ord(s2[idx]) - ord('a')] += 1
            freq2[ord(s2[idx - length]) - ord('a')] -= 1

            if freq2 == freq1:
                return True
        return False