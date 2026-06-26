class CountSquares:

    def __init__(self):
        self.points = {}
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] = self.points.get((x, y), 0) + 1       

    def count(self, point: List[int]) -> int:
        ans = 0
        qx, qy = point
        for p in self.points:
            x, y = p
            if abs(x - qx) != abs(y - qy) or x == qx:
                continue
            if (qx, y) in self.points and (x, qy) in self.points:
                ans += self.points[(qx, y)] * self.points[(x, qy)] * self.points[(x, y)]
        return ans

        
