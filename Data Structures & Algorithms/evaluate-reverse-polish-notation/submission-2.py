class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isnumeric() or i[1:].isnumeric():
                stack.append(int(i))
            else:
                second = stack.pop()
                first = stack.pop()

                if i == "+":
                    stack.append(first + second)
                elif i == "-":
                    stack.append(first - second)
                elif i == "*":
                    stack.append(first * second)
                else:
                    if first * second > 0:
                        stack.append(first // second)
                    else:
                        stack.append(abs(first) // abs(second) * -1)
                    
            print(stack)
                
        return stack[-1]