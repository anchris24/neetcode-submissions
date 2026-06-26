class Solution:
    def isPalindrome(self, s: str) -> bool:
        cut = ""
        for ch in s:
            if ord('A') <= ord(ch) <= ord('Z') or ord('a') <= ord(ch) <= ord('z') or ord('0') <= ord(ch) <= ord('9'):
                cut += ch
        cut = cut.lower()
        # print(cut)
        for i in range(len(cut)//2):
            if cut[i] != cut[len(cut) - i - 1]:
                return False
        return True

            