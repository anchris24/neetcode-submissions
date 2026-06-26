class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ['(', '{', '[']
        closes = [')', '}', ']']
        for ch in s:
            if ch in opens:
                stack.append(ch)
            else:
                if stack and stack[-1] in opens and opens.index(stack[-1]) == closes.index(ch):
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False