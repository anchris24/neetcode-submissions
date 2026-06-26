class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for op in operations:
            if op.isdigit() or (len(op) > 1 and op[1:].isdigit()):
                scores.append(int(op))

            elif op == "+":
                scores.append(scores[-2] + scores[-1])
            
            elif op == "C":
                del scores[-1]
            
            elif op == "D":
                scores.append(scores[-1] * 2)
            print(op, scores)
            
        return sum(scores)
            
