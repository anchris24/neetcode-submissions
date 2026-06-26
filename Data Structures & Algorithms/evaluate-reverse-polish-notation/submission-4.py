class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        ops = {'+', '-', '/', '*'}
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()

                if i == "+":
                    stack.append(a+b)
                elif i == "-":
                    stack.append(b-a)
                elif i == "*":
                    stack.append(a*b)
                elif i == "/":
                    stack.append(int(b/a))

        return stack[0]
