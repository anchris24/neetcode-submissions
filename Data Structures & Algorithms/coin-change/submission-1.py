class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        visited = {0:0}
        
        while visited:
            newvisit = {}
            for i, moves in visited.items():
                for c in coins:
                    if i == amount:
                        return moves
                    if i + c > amount:
                        continue
                    else:
                        newvisit[i + c] = moves + 1
            visited = newvisit
        return -1
